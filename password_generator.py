import random
from tkinter import messagebox
from tkinter import *

def generate_password():
    try:
        repeat=int(repeat_entry.get())
        length=int(length_entry.get())
    except:
        messagebox.showerror(message="Please enter in the required inputs")
        return
    if repeat==1:
        password=random.sample(character_string,length)

    else:
        password = random.choices(character_string, k=length)

    password=''.join(password)
    password_v=StringVar()
    password="Created password: "+str(password)
    password_label=Entry(password_gen,bd="0",bg="gray85",state="readonly",textvariable=password_v)
    password_label.place(x=10,y=140,height=50,width=320)

  #Define a string containing letters, symbols and numbers
character_string="ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789!#$%&'()*+,-./:;<=>?@[\]^_`{|}~"


password_gen=Tk()
password_gen.geometry("350x200")
password_gen.title("Password Generator")

    #title of the app
title_label=Label(password_gen,text="Password Generator",font=('Ubuntu Mono',12))
title_label.pack()

    #length
length_label=Label(password_gen,
text="Enter length of password: ")
length_label.place(x=20,y=30)
length_entry=Entry(password_gen,width=3)
length_entry.place(x=190,y=30)

    #repeatition
repeat_label=Label(password_gen,text="Repetition?1. No repetition , 2. Repetition")
repeat_label.place(x=20,y=60)
repeat_entry=Entry(password_gen,width=3)
repeat_entry.place(x=300,y=60)


    #call button
password_button=Button(password_gen,text="Generate Password",command=generate_password)
password_button.place(x=100,y=100)

password_gen.mainloop()
    