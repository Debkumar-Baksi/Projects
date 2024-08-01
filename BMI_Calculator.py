from tkinter import *
import tkinter as tk
from tkinter import ttk , PhotoImage
from PIL import Image , ImageTk

root=Tk()
root.title("BMI CALCULATOR")
root.geometry("550x750")
root.resizable(False,False)
root.configure(bg="#FFFFFF")

def BMI():
    h=float(Height.get())
    w=float(Weight.get())
    m=h/100
    bmi=round(float(w/m**2),1)
    label1.config(text=bmi)

    if bmi<=18.5:
        label2.config(text="Undreweight!")
        label3.config(text="You have lower weight than \n normal body!")
    elif bmi>18.5 and bmi<=25:
        label2.config(text="Normal")
        label3.config(text="It indicates that you are \n healthy.")
    elif bmi>25 and bmi<30:
        label2.config(text="Overweight!")
        label3.config(text="It indicates that a person \n is slightly overweight ! \n A doctor may advise \n to lose some weight!")
    else:
        label2.config(text="Obese!")
        label3.config(text="Health may be at risk , \n if they do not lose weight!")

#icon
image_icon = PhotoImage(file="icon.png")
root.iconphoto(False, image_icon)

#top
top_frame = Frame(root, bg="#FFDA76", width=550, height=150)
top_frame.place(x=0, y=0)
top_image = Image.open("top.png")
top_photo = ImageTk.PhotoImage(top_image)
top_label = Label(root,image=top_photo, background="#FFDA76")
top_label.place(x=35, y=-43)
text_label = Label(root, text="BMI CALCULATOR", font=("Arial", 30, "bold"), bg="#E7E8ED")
text_label.place(x=93, y=10)

#mid
mid_frame = Frame(root, bg="#FF8C9E", width=550, height=400)
mid_frame.place(x=0, y=100)

#bottom
Label(root,width=80,height=29,bg="#FF4E88").pack(side=BOTTOM)

#two boxes
box=ImageTk.PhotoImage(Image.open("box.png"))
box_label_1 = Label(root, image=box,background="#FF8C9E")
box_label_1.place(x=20, y=100)
box_label_2 = Label(root, image=box,background="#FF8C9E")
box_label_2.place(x=320, y=100)

# Headings for the boxes
height_label = Label(root, text="Height (cm)", font=("Arial", 15, "bold"), bg="#FFFFFF")
height_label.place(x=68, y=150)
weight_label = Label(root, text="Weight (kg)", font=("Arial", 15, "bold"), bg="#FFFFFF")
weight_label.place(x=368, y=150)

#scale
scale=PhotoImage(file="scale.png")
Label(root,image=scale,bg="#FF4E88").place(x=-240,y=310)


###############Slider1###############
current_value=tk.DoubleVar()


def get_current_value():
    return '{: .2f}'.format(current_value.get())
def slider_changed(event):
    Height.set(get_current_value())

    size=int(float(get_current_value()))
    img=(Image.open("man.png"))
    resized_image=img.resize((250,250+size))
    photo2=ImageTk.PhotoImage(resized_image)
    secondimage.config(image=photo2)
    secondimage.place(x=50,y=528-size)
    secondimage.image=photo2


style=ttk.Style()
style.configure("TScale",background="white")
slider=ttk.Scale(root,from_=50,to=220,orient="horizontal",style="TScale",
                 command=slider_changed,variable=current_value)
slider.place(x=72,y=248)

#####################################


##@@@@@@@@@@@@@Slider2@@@@@@@@@@@@@@@
current_value2=tk.DoubleVar()


def get_current_value2():
    return '{: .2f}'.format(current_value2.get())
def slider_changed2(event):
    Weight.set(get_current_value2())


style2=ttk.Style()
style2.configure("TScale",background="white")
slider2=ttk.Scale(root,from_=40,to=120,orient="horizontal",style="TScale",
                 command=slider_changed2,variable=current_value2)
slider2.place(x=380,y=248)

##@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

#entry box
Height=StringVar()
Weight=StringVar()

height=Entry(root,textvariable=Height,width=6,font='arial 25',bg='#fff',fg='#000',bd=0,justify=CENTER)
height.place(x=61,y=180)
Height.set(get_current_value())

weight=Entry(root,textvariable=Weight,width=6,font='arial 25',bg='#fff',fg='#000',bd=0,justify=CENTER)
weight.place(x=361,y=180)
Weight.set(get_current_value2())

#man image
secondimage=Label(root,bg="#FF4E88")
secondimage.place(x=70,y=530)

Button(root,text="View Report",width=15,height=2,font="arial 10 bold" , bg="#1f6e68" , fg="white",command=BMI ).place(x=400,y=330)

label1=Label(root,font="arial 40 bold" , bg="#FF4E88" , fg="#fff")
label1.place(x=230,y=320)

label2=Label(root,font="arial 20 bold" , bg="#FF4E88" , fg="#3b3a3a")
label2.place(x=340,y=430)

label3=Label(root,font="arial 15 bold" , bg="#FF4E88")
label3.place(x=280,y=500)

root.mainloop()
