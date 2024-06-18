__author__ = "Triparna Mandal"
import pyqrcode
import qrcode
import random
import tkinter as tk 
from tkinter import *
from tkinter import messagebox
from PIL import ImageTk, Image

#Defining CreateWidgets() function to create necessary tkinter widgets
def CreateWidgets():
    label = Label(text='Enter Text: ',bg='azure')
    label.grid(row=0, column=1, padx=5, pady=5)

    root.entry = Entry(width=30, textvariable=qrInput)
    root.entry.grid(row=0, column=2, padx=5, pady=5)

    button = Button(width=10, text='Generate', command=QRCodeGenerate)
    button.grid(row=0, column=3, padx=5, pady=5)

    label = Label(text='QR Code: ', bg='azure')
    label.grid(row=1, column=1, padx=5, pady=5)

    root.imageLabel = Label(root, background='azure')
    root.imageLabel.grid(row=2, column=1, columnspan=2, padx=5, pady=5)

#defining QRCodeGenerate() fun
def QRCodeGenerate():
    # Storing user-input text in a var
    qrString = qrInput.get()
    
    string="0123456789abcdefghjklmnopqrstuvwyzABCDEFGHIJKLMNOPQRSTUVWYZ"
    num=random.choice(string)

    if qrString!='':
        qrGenerate = pyqrcode.create(qrString)

        # qrCodePath = 'D:\qrcodess'
        qrCodeName = qrString + "QR" + ".png"
        #install pypng module using pip command
        qrGenerate.png(qrCodeName, scale=6)
        image = Image.open(qrCodeName)
        image = image.resize((400,400), Image.ANTIALIAS)

        image = ImageTk.PhotoImage(image)
        root.imageLabel.config(image=image)
        root.imageLabel.photo = image

    else: 
        messagebox.showerror("ERROR","ENTER A TEXT!")

root = tk.Tk()
root.title("QRCODE GENERATOR")
root.geometry('510x500')
root.resizable(False,False)
root.config(background='azure')

qrInput = StringVar()
CreateWidgets()
root.mainloop()