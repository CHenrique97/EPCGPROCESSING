from Processing import *
import PIL as pil
from PIL import ImageTk



from tkinter import *
def clicked():
  
  orgimg = img_converter(txt.get())
  print(txt.get())
  procpic1 = array_to_img(simulate(orgimg))
  procpic1.save("imgd.jpg")
  procpic2 = array_to_img(simulate(orgimg,color_deficit="p"))
  procpic2.save("imgp.jpg")
  procpic3 = array_to_img(simulate(orgimg,color_deficit='t'))
  procpic3.save("imgt.jpg")
  img = ImageTk.PhotoImage(pil.Image.open("imgd.jpg").resize((100,100)))
  imgN = ImageTk.PhotoImage(pil.Image.open(txt.get()).resize((100,100)))
  imgt = ImageTk.PhotoImage(pil.Image.open("imgt.jpg").resize((100,100)))
  imgp = ImageTk.PhotoImage(pil.Image.open("imgp.jpg").resize((100,100)))
  gambiN.configure(image=imgN)
  gambiN.image=imgN
  gambiP.configure(image=imgp)
  gambiP.image=imgp
  gambiD.configure(image=img)
  gambiD.image=img
  gambiT.configure(image=imgt)
  gambiT.image=imgt
window = Tk()

window.title("Daltonismo")
window.geometry('600x200')
lbl = Label(window,text="Coloque o nome da Imagem")
lblN = Label(window,text="Normal")
lblP = Label(window,text="Protantopia")
lblD = Label(window,text="Deuteranopia")
lblT = Label(window,text="Tritanopia")
lbl.grid(column=0, row=0)
txt = Entry(window,width=10)
txt.grid(column=1, row=0)
#Creates a Tkinter-compatible photo image, which can be used everywhere Tkinter expects an image object.
img = ImageTk.PhotoImage(pil.Image.open("imgd.jpg").resize((100,100)))
imgN = ImageTk.PhotoImage(pil.Image.open("img.jpeg").resize((100,100)))
imgt = ImageTk.PhotoImage(pil.Image.open("imgt.jpg").resize((100,100)))
imgp = ImageTk.PhotoImage(pil.Image.open("imgp.jpg").resize((100,100)))
btn = Button(window, text="Clique aqui", command=clicked)
gambiN=Label(window,image=imgN)
gambiP=Label(window,image=imgp)
gambiD=Label(window,image=img)
gambiT=Label(window,image=imgt)
btn.grid(column=2, row=0)
lblN.grid(column=0,row=1)
lblP.grid(column=1,row=1)
lblD.grid(column=2,row=1)
lblT.grid(column=3,row=1)
gambiN.grid(column=0,row=2)
gambiP.grid(column=1,row=2)
gambiD.grid(column=2,row=2)
gambiT.grid(column=3,row=2)
window.mainloop()