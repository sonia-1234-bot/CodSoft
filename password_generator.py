import random
import pyperclip
from tkinter import *
root=Tk()
root.title("Password Generator")
root.geometry("300x300")

label1=Label(root, text="Enter the length of the password: ")
label1.pack(pady=20)

entry=Entry(root,width=30,borderwidth=5)
entry.pack(padx=20,pady=20)

def password_generator():
    entry1.delete(0,END)
    len=entry.get()
    chars='abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    num='1234567890'
    s = "!@#$%&*"
    password=[]
    combined=chars+num+s
    entry.delete(0,END)
    for i in range(int(len)):
        password.append(random.choice(combined))
    password1=''.join(password)    
    entry1.insert(0,password1)

mybutton=Button(root,text="Generate",command=lambda:password_generator())
mybutton.pack()

entry1=Entry(root,width=30,borderwidth=5)
entry1.pack(padx=20,pady=20)

def copy_text():
    text_to_copy=entry1.get()
    pyperclip.copy(text_to_copy)

mybutton=Button(root,text="COPY",command=copy_text)
mybutton.pack()

root.mainloop()