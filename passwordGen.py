
from tkinter import *
import string
import random
import pyperclip

def generator():
    upper = string.ascii_uppercase
    lower = string.ascii_lowercase
    digit = string.digits
    pun = string.printable
    conbine = upper + lower + digit + pun
            
    password_length = int(length_box.get())

    Password = random.sample(conbine,password_length)
    password_life.insert(0,Password)

def copy():
    copy_password = password_life.get()
    pyperclip.copy(copy_password)

    

root = Tk()
root.title("Random Password Generator")
root.config(bg="orange")
root.geometry("500x500")

password_label = Label(text="Random Password Generator", font="comicsonsms 20 bold")
password_label.place(x=30,y=40,height=40,width=400)

length_label = Label(root,text="Password Length", font="comicsonsms 20 bold ")
length_label.place(x=100,y=100,height=40,width=300)

length_box = Spinbox(root, from_=5,to=18, font="comicsonsms 20 bold ")
length_box.place(x=200, y=180,height=40, width=50)

generate_button = Button(root,text="Generate", font="comicsonsms 20 bold", command=generator)
generate_button.place(x=120,y=240,height=40,width=220)

password_life = Entry(root,font="comicsonsms 15 ")
password_life.place(x=30,y=300, height=40, width=400)

copy_button = Button(root,text="Copy", font="comicsonsms 20 bold",command=copy)
copy_button.place(x=120,y=360,height=40,width=220)

root.mainloop()


