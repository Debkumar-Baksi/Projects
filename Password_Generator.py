from tkinter import *
import string
import random
import pyperclip



def generator():
    small_alphabets=string.ascii_lowercase
    capital_alphabets=string.ascii_uppercase
    numbers=string.digits
    special_characters=string.punctuation

    all=small_alphabets+capital_alphabets+numbers+special_characters
    password_length=int(length_box.get())

    if choice.get()==1:
        password_field.insert(0,random.sample(small_alphabets,password_length))

    if choice.get()==2:
        password_field.insert(0,random.sample(small_alphabets+capital_alphabets+numbers,
                                              password_length))

    if choice.get()==3:
        password_field.insert(0,random.sample(all,password_length))


def copy():
    random_passsword=password_field.get()
    pyperclip.copy(random_passsword)

root=Tk()
root.config(bg="gray20")
choice=IntVar()
Font=("arial",13,"bold")
password_label=Label(root,text="PASSWORD GENERATOR",
                     font=("times new roman",20,"bold"),
                     bg="gray20",fg="white")
password_label.grid(pady=10)

weak_radio_button=Radiobutton(root,text="Weak",value=1,
                              variable=choice,font=Font)
weak_radio_button.grid(pady=5)


medium_radio_button=Radiobutton(root,text="Medium",value=2,
                              variable=choice,font=Font)
medium_radio_button.grid(pady=5)


strong_radio_button=Radiobutton(root,text="Strong",value=3,
                              variable=choice,font=Font)
strong_radio_button.grid(pady=5)

length_label=Label(root,text="Password Length",
                     font=Font,
                     bg="gray20",fg="white")
length_label.grid(pady=10)


length_box=Spinbox(root,from_=5,to_=18,width=5,font=Font)
length_box.grid(pady=5)

generate_button=Button(root,text="Generate",font=Font,
                       command=generator)
generate_button.grid(pady=5)

password_field=Entry(root,width=25,bd=2,font=Font)
password_field.grid(pady=5)

copy_button=Button(root,text="Copy",font=Font,command=copy)
copy_button.grid(pady=5)




root.mainloop()
