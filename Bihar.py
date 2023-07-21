
from tkinter import *
from PIL import ImageTk,Image
import tkinter as tk



def Start():
    b = tk.Tk()
    b.geometry("1800x850")
    frame_1 =Frame(b,width = 1800,height=950)

    frame_1.place(anchor='center',relx=0.5,rely=0.5)

    im = Image.open("54.jpg")
    img_1 =ImageTk.PhotoImage(im)

    label_1 = Label(frame_1,image=img_1)

    chat_1 = Label(b,text="BIHAR ME AAPKA SWAGAT HAI",bg='snow1',fg='red')
    chat_1.config(font = ("Times New Roman",25))

    b.title('BIHAR')

    btn1 = Button(b,text="GAYA",bg='snow2', fg='red',font=('Courier',20),activebackground='black',activeforeground='medium orchid', command=Gaya)
    btn1.place(relx=0.01,rely=0.12, relwidth=0.15,relheight=0.1)
        
    btn2 = Button(b,text="BODH GAYA",bg='snow2', fg='red',font=('Courier',20),activebackground='black',activeforeground='medium orchid', command=b.destroy)
    btn2.place(relx=0.01,rely=0.26, relwidth=0.15,relheight=0.1)
        
    btn3 = Button(b,text="SITAMANI",bg='snow2', fg='red',font=('Courier',20),activebackground='black',activeforeground='medium orchid', command=b.destroy)
    btn3.place(relx=0.01,rely=0.40,relwidth=0.15,relheight=0.1)
        
    btn4 = Button(b,text="PATNA",bg='snow2', fg='red',font=('Courier',20),activebackground='black',activeforeground='medium orchid', command = b.destroy)
    btn4.place(relx=0.01,rely=0.54, relwidth=0.15,relheight=0.1)
        
    btn5 = Button(b,text="NALANDA",bg='snow2', fg='red',font=('Courier',20),activebackground='black',activeforeground='medium orchid', command = b.destroy)
    btn5.place(relx=0.01,rely=0.68, relwidth=0.15,relheight=0.1)

    btn5 = Button(b,text="DARBHANGA",bg='snow2', fg='red',font=('Courier',20),activebackground='black',activeforeground='medium orchid', command = b.destroy)
    btn5.place(relx=0.01,rely=0.82, relwidth=0.15,relheight=0.1)

    #btn6 = Button(b,text="RAJGIR",bg='snow2', fg='red',font=('Courier',20),activebackground='black',activeforeground='medium orchid', command = b.destroy)
    #btn6.place(relx=0.82,rely=0.12, relwidth=0.15,relheight=0.1)



    #btn8 = Button(b,text="Search Reader",bg='black', fg='white', font=('Courier',20),command = b.destroy)
    #btn8.place(relx=0.35,rely=0.80, relwidth=0.35,relheight=0.1)

    #btn9 = Button(b,text="Delete Reader",bg='black', fg='white', font=('Courier',20),command = b.destroy)
    #btn9.place(relx=0.40,rely=0.90, relwidth=0.35,relheight=0.1)

    #btn10 = Button(b,text="QUIT",bg='black', fg='white', font=('Courier',20),command = b.destroy)
    #btn10.place(relx=0.45,rely=1.00, relwidth=0.35,relheight=0.1)

        
    chat_1.pack()
    chat_1.place(relx=0.62,rely=0.029, relwidth=0.40, relheight=0.08)
    frame_1.pack()
    label_1.pack()
    b.mainloop()

def Gaya():
    a = tk.Toplevel()

    a.geometry("1800x850")
    frame =Frame(a,width = 1800,height=950)

    frame.place(anchor='center',relx=0.5,rely=0.5)


    img =ImageTk.PhotoImage(Image.open("tower.png"))

    label = Label(frame,image=img)

    chat = Label(a,text="   GAYA   ",bg='snow2')
    chat.config(font = ("Times New Roman",45))

    a.title('TOURISM')


        

    button = tk.Button(a,text="Let's Start the Journey",bg='PeachPuff2',width=25,activebackground='black',activeforeground='medium orchid',command=a.destroy)





    button.pack()
    button.place(relx=0.82,rely=0.89, relwidth=0.20,relheight=0.05)
    chat.pack()
    chat.place(relx=0.38,rely=0.029, relwidth=0.20, relheight=0.08)
    frame.pack()
    label.pack()
    a.mainloop()

Start()

            
