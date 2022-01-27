from cgitb import text
import PIL
from PIL import Image
from tkinter import *
from tkinter.filedialog import *

root = Tk()
root.title("Image Compressor")
root.geometry('300x300')
root.config(bg='white')

def comp():
    file_path = askopenfilename()
    img = PIL.Image.open(file_path)
    max_width,max_height = img.size

    img = img.resize((max_width,max_height),PIL.Image.ANTIALIAS)
    save_path = asksaveasfilename()
    img.save(save_path+"Compress.jpg")

btn = Button(root,text='Select File',width=12,height=2,bg='teal',command=comp)
btn.pack(anchor=CENTER,pady=70)

btn2 = Button(root,text='Close',width=12,height=2,bg='red',command=lambda:exit())
btn2.pack(anchor=CENTER,pady=2)

root.mainloop()


# Mohit

