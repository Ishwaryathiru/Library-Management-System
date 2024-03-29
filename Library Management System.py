from tkinter import *  #library tkinter
from tkinter import messagebox
a=Tk()
a.geometry("500x500")  #size
a.title("LIBRARY STUDENT PORTAL") #title

def instruct():
    m=messagebox.showwarning("welcome to library","Logout once u leave")

def show():
    lb=Listbox(a)    #list box
    lb.insert(1,"Tech Mat")
    lb.insert(2,"Tech phy")
    lb.insert(3,"Tech chem")
    lb.insert(4,"Tech Eng")
    lb.insert(END)
    lb.pack()
    lb.get(ACTIVE) #get active
    def confrim():
        l2=Label(a,text="")
        l2.pack()
        l2.config(text=lb.get(ANCHOR))
        def out():
            m=messagebox.showinfo("Logging out....","Successfully logged out")
        b4=Button(a,text="Logout",command=out)
        b4.pack()
    b3=Button(a,text="I confirm",command=confrim)
    b3.pack()

def gen():
    b1=Button(a,text="Instruction",fg="white",bg="black",command=instruct,font=12,padx=5,pady=7)
    b2=Button(a,text="show book",padx=9,pady=7,fg="white",bg="black",command=show,font=12)#button
    b1.pack()
    b2.pack()#button pack
    a.mainloop()

l=Label(a,text="BOOK RETURN ENTRY",bg="blue",fg="white",font=("Bold",25)) #label
l.pack()
n=LabelFrame(a,text="Enter name",padx=10,pady=8)
n.pack(padx=12,pady=15)
e=Entry(n)
b=Button(a,text="Login",bg="blue",fg="white",command=gen)
b.pack()
e.pack()

a.mainloop()