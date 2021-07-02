from PIL import Image,ImageFilter
import numpy as np  

        



def transform_colorspace(img, mat):

    return np.einsum("ij, ...j", mat, img, dtype=np.float16, casting="same_kind")

def inverse_gamma_correction(linear_rgb, gamma=2.4):

    rgb = np.zeros_like(linear_rgb, dtype=np.float16)
    for i in range(3):
        idx = linear_rgb[:, :, i] <= 0.0031308
        rgb[idx, i] = 255 * 12.92 * linear_rgb[idx, i]
        idx = np.logical_not(idx)
        rgb[idx, i] = 255 * (1.055 * linear_rgb[idx, i]**(1/gamma) - 0.055)
    return np.round(rgb)


def gamma_correction(rgb, gamma=2.4):

    linear_rgb = np.zeros_like(rgb, dtype=np.float16)
    for i in range(3):
        idx = rgb[:, :, i] > 0.04045 * 255
        linear_rgb[idx, i] = ((rgb[idx, i] / 255 + 0.055) / 1.055)**gamma
        idx = np.logical_not(idx)
        linear_rgb[idx, i] = rgb[idx, i] / 255 / 12.92
    return linear_rgb

def simulate(rgb, color_deficit="d"):

    cb_matrices = {
        "d": np.array([[1, 0, 0], [1.10104433,  0, -0.00901975], [0, 0, 1]], dtype=np.float16),
        "p": np.array([[0, 0.90822864, 0.008192], [0, 1, 0], [0, 0, 1]], dtype=np.float16),
        "t": np.array([[1, 0, 0], [0, 1, 0], [-0.15773032,  1.19465634, 0]], dtype=np.float16),
    }
    rgb2lms = np.array([[0.3904725 , 0.54990437, 0.00890159],
    [0.07092586, 0.96310739, 0.00135809],
    [0.02314268, 0.12801221, 0.93605194]], dtype=np.float16)
    lms2rgb = np.array([[ 2.85831110e+00, -1.62870796e+00, -2.48186967e-02],
    [-2.10434776e-01,  1.15841493e+00,  3.20463334e-04],
    [-4.18895045e-02, -1.18154333e-01,  1.06888657e+00]], dtype=np.float16)

    lms = transform_colorspace(rgb, rgb2lms)

    sim_lms = transform_colorspace(lms, cb_matrices[color_deficit])

    sim_rgb = transform_colorspace(sim_lms, lms2rgb)
    return sim_rgb

def clip_array(arr, min_value=0, max_value=255):

    comp_arr = np.ones_like(arr)
    arr = np.maximum(comp_arr * min_value, arr)
    arr = np.minimum(comp_arr * max_value, arr)
    return arr
def array_to_img(arr, gamma=2.4):

    arr = inverse_gamma_correction(arr, gamma=gamma)
    arr = clip_array(arr)
    arr = arr.astype('uint8')
    img = Image.fromarray(arr, mode='RGB')
    return img
def img_converter(img_address):
    img = np.asarray(Image.open(img_address).convert("RGB"), dtype=np.float16)
    return gamma_correction(img,2.4)

