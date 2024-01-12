from tkinter import *
from PIL import Image,ImageTk
from tkinter import messagebox
win=Tk()
win.geometry("600x500")
win.resizable(0,0)
win.config(background="grey")
win.title("Login")
def sub():
    cw=Toplevel(win)
    cw.geometry("1350x800")
    cw.config(background="blue")
    cw.title("KVS MART")
    l1=Label(cw,text="K.V.S. Mart",bg="blue",fg="white",font=("monotype corsiva",40,"bold"))
    l1.place(x=180,y=10)
    img=Image.open("C:\\Users\\vikash\\Desktop\\man.png")
    i=img.resize((100,80))
    im=ImageTk.PhotoImage(i)
    l2=Label(cw,image=im)
    l2.pack()



l1=Label(win,text="LOGIN PROCESS",bg="grey",fg="blue",font=("algerian",24,"bold"))
l1.pack(pady=10)
l2=Label(win,text="UserName",bg="grey",fg="black",font=("monotype corsiva",20,"bold"))
l2.place(x=230,y=70)
e1=Entry(win,bg="white",fg="black",font=("clarity",20,"bold"),bd=7)
e1.place(x=145,y=120)
l3=Label(win,text="Password",bg="grey",fg="black",font=("monotype corsiva",20,"bold"))
l3.place(x=230,y=190)
e2=Entry(win,bg="white",fg="black",font=("clarity",20,"bold"),bd=7)
e2.place(x=145,y=240)
b1=Button(win,text="SUBMITT",bg="green",fg="white",font=("algerian",14,"bold"),bd=10,command=sub)
b1.place(x=230,y=320)





win.mainloop() 