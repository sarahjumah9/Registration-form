from tkinter import *

from pkg_resources import EntryPoint
root = Tk()
root.geometry("500x300")
def confirmval():
    print("You have successfully registered! Thank you!")

Label(root, text="REGISTRATION FORM", font="ar 15 bold").grid(row=0, column=3)

name = Label(root, text="Name: ").grid(row=1, column=2)
admission_number = Label(root, text="Admisssion Number: ").grid(row=2, column=2)
gender = Label(root, text="Gender: ").grid(row=3, column=2)
telephone = Label(root, text="Telephone: ").grid(row=4, column=2)

namevalue = StringVar
admission_numbervalue = StringVar
gendervalue = StringVar
telephonevalue = StringVar
checkvalue = IntVar

nameentry = Entry(root, text= namevalue).grid(row=1 , column=3)
admission_numberentry = Entry(root, text=admission_numbervalue).grid(row=2, column=3)
genderentry = Entry(root, text=gendervalue).grid(row=3, column=3)
telephoneentry = Entry(root,text=telephonevalue ).grid(row=4, column=3)

checkbutton = Checkbutton(text= " Log in ", variable= checkvalue).grid(row=5, column=3)

Button(text= "Submit", command=confirmval).grid(row=6, column=3)
root.mainloop()