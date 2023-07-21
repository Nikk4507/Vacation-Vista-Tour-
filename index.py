from tkinter import *
from turtle import left
from PIL import ImageTk,Image
import tkinter as tk
import mysql.connector
from tkinter import messagebox


def View_Res():
    mydb = mysql.connector.connect(
      host="localhost",
      user="root",
      password="root",
      database="Tourism"
    )
    mycursor = mydb.cursor()

    root = Tk()
    root.title("TOURISM")
    root.minsize(width=400,height=400)
    root.geometry("1200x800")

    Canvas1 = Canvas(root) 
    Canvas1.config(bg="black")
    Canvas1.pack(expand=True,fill=BOTH)

    headingFrame1 = Frame(root,bg="black",bd=5)
    headingFrame1.place(relx=0.25,rely=0.1,relwidth=0.5,relheight=0.13)

    headingLabel = Label(headingFrame1, text="RESTURANTS", bg='cyan', fg='black', font = ('Courier',20))

    headingLabel.place(relx=0,rely=0, relwidth=1, relheight=1)

    labelFrame = Frame(root,bg='black')
    labelFrame.place(relx=0.05,rely=0.3,relwidth=0.9,relheight=0.5)
    y = 0.25

    Label(labelFrame, text="%-15s%-25s%-30s%-25s"%('S.no',' NAME','PHONE NUMBER','ADDRESS'),
    bg='black',fg='red',font = ('Courier',12,'bold')).place(relx=0.07,rely=0.1)
    Label(labelFrame, text = "----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------",bg='black',fg='red').place (relx=0.05,rely=0.2)
    R = "select * from resturants"
    try:
        mycursor.execute(R)
    


        for i in mycursor:
            Label(labelFrame,text="%-10s%-45s%-20s%-20s"%(i[0],i[1],i[3],i[2]) ,bg='black', fg='red',font = ('Courier',10,'bold')).place(relx=0.07,rely=y)
            y += 0.1
    except:
        messagebox.showinfo("Failed to fetch files from database")
    
    quitBtn = Button(root,text="Quit",bg='#FF5733', fg='black', command=root.destroy)
    quitBtn.place(relx=0.4,rely=0.9, relwidth=0.18,relheight=0.08)
    
    root.mainloop()



def resturants():
    a = tk.Toplevel()

    a.geometry("1800x850")
    a.configure(bg='black')

    chat = Button(a,text="  RESTURANTS  ",bg='light pink',command=View_Res)
    chat.config(font = ("Times New Roman",65))
    chat_1=Label(a,text="'CLICK RESTURANT! FOR INFO'",bg='light pink')
    chat_1.config(font = ("Times New Roman",12))

    a.title('RESTURANT')
    #1
    img_1 =ImageTk.PhotoImage(Image.open("cafe_11.jpg"))

    btn1 = Button(a,image=img_1, command = NONE)
    # Set a relative position of button
    btn1.pack(side='top',padx=50,pady=10,anchor=NW)

    #2
    img_2 =ImageTk.PhotoImage(Image.open("cafe_22.jpg"))

    btn2 = Button(a,image=img_2, command = NONE)
    # Set a relative position of button
    btn2.pack(side='bottom',padx=50,pady=80,anchor=SW)

    button = tk.Button(a,text="EXIT",bg='light pink',width=25,activebackground='black',activeforeground='medium orchid',command=a.destroy)
    button.pack()
    button.place(relx=0.79,rely=0.89, relwidth=0.20,relheight=0.05)


    
    
 

    
    chat.pack()
    chat.place(relx=0.58,rely=0.39, relwidth=0.40, relheight=0.1)
    chat_1.pack()
    chat_1.place(relx=0.58,rely=0.49, relwidth=0.40, relheight=0.015)
    
    
    a.mainloop()



def View():
    mydb = mysql.connector.connect(
      host="localhost",
      user="root",
      password="root",
      database="tOURISM"
    )
    mycursor = mydb.cursor()

    root = Tk()
    root.title("CAFETERIA_1")
    root.minsize(width=400,height=400)
    root.geometry("1800x900")

    Canvas1 = Canvas(root) 
    Canvas1.config(bg="black")
    Canvas1.pack(expand=True,fill=BOTH)

    headingFrame1 = Frame(root,bg="black",bd=5)
    headingFrame1.place(relx=0.25,rely=0.1,relwidth=0.5,relheight=0.13)

    headingLabel = Label(headingFrame1, text="CAFETERIA", bg='cyan', fg='black', font = ('Courier',20))

    headingLabel.place(relx=0,rely=0, relwidth=1, relheight=1)

    labelFrame = Frame(root,bg='black')
    labelFrame.place(relx=0.05,rely=0.3,relwidth=0.9,relheight=0.5)
    y = 0.25

    Label(labelFrame, text="%-10s%-10s%-35s%-25s"%('S.no',' NAME','PHONE NUMBER','ADDRESS'),
    bg='black',fg='red',font = ('Courier',12,'bold')).place(relx=0.07,rely=0.1)
    Label(labelFrame, text = "----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------",bg='black',fg='red').place (relx=0.05,rely=0.2)
    C = "select * from cafeteria"
    try:
        mycursor.execute(C)
    


        for i in mycursor:
            Label(labelFrame,text="%-10s%-20s%-25s%-20s"%(i[0],i[1],i[3],i[2]) ,bg='black', fg='red',font = ('Courier',10,'bold')).place(relx=0.07,rely=y)
            y += 0.1
    except:
        messagebox.showinfo("Failed to fetch files from database")
    
    def First():  
        b = tk.Toplevel()
        b.geometry("1800x850")
        b.configure(bg='black')
        frame_1 =Frame(b,width = 1800,height=950)

        frame_1.place(anchor='center',relx=0.5,rely=0.5)

        img =ImageTk.PhotoImage(Image.open("coffe_roaster1.png"))
        label_1 = Label(frame_1,image=img,bg='black')


        chat_1 = Label(b,text="COFFEE ROASTER CAFE",bg='black',fg='red')
        chat_1.config(font = ("Times New Roman",23))

        b.title('CAFE_1')
        chat_1.pack()
        chat_1.place(relx=0.35,rely=0.79, relwidth=0.30, relheight=0.08)
        dltBtn = Button(b,text="Quit",bg='black', fg='red', command=b.destroy)
        dltBtn.place(relx=0.75,rely=0.79, relwidth=0.18,relheight=0.08)
        frame_1.pack()
        label_1.pack()

        b.mainloop()

    def Sec():  
        b = tk.Toplevel()
        b.geometry("1800x850")
        b.configure(bg='black')
        frame_1 =Frame(b,width = 1800,height=950)

        frame_1.place(anchor='center',relx=0.5,rely=0.5)

        img =ImageTk.PhotoImage(Image.open("snook_house.png"))
        label_1 = Label(frame_1,image=img,bg='black')


        chat_1 = Label(b,text="SNOOK'S HOUSE CAFE",bg='black',fg='red')
        chat_1.config(font = ("Times New Roman",23))

        b.title('CAFE_2')
        chat_1.pack()
        chat_1.place(relx=0.35,rely=0.79, relwidth=0.30, relheight=0.08)
        dltBtn = Button(b,text="Quit",bg='black', fg='red', command=b.destroy)
        dltBtn.place(relx=0.75,rely=0.79, relwidth=0.18,relheight=0.08)
        frame_1.pack()
        label_1.pack()

        b.mainloop()

    def Third():  
        b = tk.Toplevel()
        b.geometry("1800x850")
        b.configure(bg='black')
        frame_1 =Frame(b,width = 1800,height=950)

        frame_1.place(anchor='center',relx=0.5,rely=0.5)

        img =ImageTk.PhotoImage(Image.open("the_freak.png"))
        label_1 = Label(frame_1,image=img,bg='black')


        chat_1 = Label(b,text="THE FREAK CAFE",bg='black',fg='red')
        chat_1.config(font = ("Times New Roman",23))

        b.title('CAFE_3')
        chat_1.pack()
        chat_1.place(relx=0.35,rely=0.79, relwidth=0.30, relheight=0.08)
        dltBtn = Button(b,text="Quit",bg='black', fg='red', command=b.destroy)
        dltBtn.place(relx=0.75,rely=0.79, relwidth=0.18,relheight=0.08)
        frame_1.pack()
        label_1.pack()

        b.mainloop()

    def Four():  
        b = tk.Toplevel()
        b.geometry("1800x850")
        b.configure(bg='black')
        frame_1 =Frame(b,width = 1800,height=950)

        frame_1.place(anchor='center',relx=0.5,rely=0.5)

        img =ImageTk.PhotoImage(Image.open("MNC.png"))
        label_1 = Label(frame_1,image=img,bg='black')


        chat_1 = Label(b,text="MOMO NATION CAFE",bg='black',fg='red')
        chat_1.config(font = ("Times New Roman",23))

        b.title('CAFE')
        chat_1.pack()
        chat_1.place(relx=0.35,rely=0.79, relwidth=0.30, relheight=0.08)
        dltBtn = Button(b,text="Quit",bg='black', fg='red', command=b.destroy)
        dltBtn.place(relx=0.75,rely=0.79, relwidth=0.18,relheight=0.08)
        frame_1.pack()
        label_1.pack()

        b.mainloop()
    


    
    btn1 = Button(root,text="click",command=First)
    btn1.place(relx=0.7,rely=0.43, relwidth=0.02,relheight=0.02)

    btn2 = Button(root,text="click",command=Sec)
    btn2.place(relx=0.81,rely=0.48, relwidth=0.02,relheight=0.02)

    btn3 = Button(root,text="click",command=Third)
    btn3.place(relx=0.73,rely=0.53, relwidth=0.02,relheight=0.02)

    btn4 = Button(root,text="click",command=Four)
    btn4.place(relx=0.86,rely=0.58, relwidth=0.02,relheight=0.02)


    quitBtn = Button(root,text="Quit",bg='#FF5733', fg='black', command=root.destroy)
    quitBtn.place(relx=0.4,rely=0.9, relwidth=0.18,relheight=0.08)

    root.mainloop()


def cafeteria():
    a = tk.Toplevel()

    a.geometry("1800x850")
    a.configure(bg='black')

    chat = Button(a,text="  CAFETERIA  ",bg='light pink',command=View)
    chat.config(font = ("Times New Roman",65))
    chat_1=Label(a,text="'CLICK CAFETERIA! FOR INFO'",bg='light pink')
    chat_1.config(font = ("Times New Roman",12))

    a.title('CAFETERIA')
    #1
    img_1 =ImageTk.PhotoImage(Image.open("cafe_11.jpg"))

    btn1 = Button(a,image=img_1, command = NONE)
    # Set a relative position of button
    btn1.pack(side='top',padx=50,pady=10,anchor=NW)

    #2
    img_2 =ImageTk.PhotoImage(Image.open("cafe_22.jpg"))

    btn2 = Button(a,image=img_2, command = NONE)
    # Set a relative position of button
    btn2.pack(side='bottom',padx=50,pady=80,anchor=SW)

    button = tk.Button(a,text="EXIT",bg='light pink',width=25,activebackground='black',activeforeground='medium orchid',command=a.destroy)
    button.pack()
    button.place(relx=0.79,rely=0.89, relwidth=0.20,relheight=0.05)


    
    
 

    
    chat.pack()
    chat.place(relx=0.58,rely=0.39, relwidth=0.40, relheight=0.1)
    chat_1.pack()
    chat_1.place(relx=0.58,rely=0.49, relwidth=0.40, relheight=0.015)
    
    
    a.mainloop()




def Gaya():
    a = tk.Toplevel()

    a.geometry("1800x850")
    a.configure(bg='black')
    frame =Frame(a,width = 1800,height=950)

    frame.place(anchor='center',height=1500,relx=0.5,rely=0.5)


    img =ImageTk.PhotoImage(Image.open("V_gaya.jpg"))

    label = Label(frame,image=img,bg='black')

    chat = Label(a,text="  GAYA  ",bg="black",fg="red")
    chat.config(font = ("Times New Roman",48))

    a.title('GAYA')


        

    button = tk.Button(a,text="EXIT",bg='light pink',width=25,activebackground='black',activeforeground='medium orchid',command=a.destroy)

    btn1 = Button(a,text="CAFETERIA",bg='light pink', fg='black',font=("Times New Roman",16),activebackground='black',activeforeground='medium orchid', command=cafeteria)
    btn1.place(relx=0.01,rely=0.12, relwidth=0.12,relheight=0.1)
        
    btn2 = Button(a,text="RESTURANTS",bg='light pink', fg='black',font=("Times New Roman",16),activebackground='black',activeforeground='medium orchid', command=resturants)
    btn2.place(relx=0.01,rely=0.40, relwidth=0.12,relheight=0.1)
        
    btn3 = Button(a,text="SHOPPING MALL",bg='light pink', fg='black',font=("Times New Roman",16),activebackground='black',activeforeground='medium orchid', command=a.destroy)
    btn3.place(relx=0.01,rely=0.70,relwidth=0.12,relheight=0.1)
        
    btn4 = Button(a,text="TEMPLE",bg='light pink', fg='black',font=("Times New Roman",16),activebackground='black',activeforeground='medium orchid', command = a.destroy)
    btn4.place(relx=0.86,rely=0.12, relwidth=0.12,relheight=0.1)
        
    btn5 = Button(a,text="COLLEGE\n AND \nSCHOOL",bg='light pink', fg='black',font=("Times New Roman",15),activebackground='black',activeforeground='medium orchid', command = a.destroy)
    btn5.place(relx=0.86,rely=0.40, relwidth=0.12,relheight=0.1)

    btn5 = Button(a,text="WARD COUNCLER",bg='light pink', fg='black',font=("Times New Roman",16),activebackground='black',activeforeground='medium orchid', command = a.destroy)
    btn5.place(relx=0.86,rely=0.70, relwidth=0.12,relheight=0.1)



    button.pack()
    button.place(relx=0.86,rely=0.89, relwidth=0.15,relheight=0.05)
    chat.pack()
    chat.place(relx=0.34,rely=0.83, relwidth=0.30, relheight=0.08)
    frame.pack()
    label.pack()
   
    a.mainloop()



    

def Start():
    b = tk.Toplevel()
    b.geometry("1800x850")
    b.configure(bg='black')
    frame_1 =Frame(b,width = 1800,height=950)

    frame_1.place(anchor='center',relx=0.5,rely=0.5)

    img =ImageTk.PhotoImage(Image.open("544.jpg"))
    label_1 = Label(frame_1,image=img,bg='black')


    chat_1 = Label(b,text="BIHAR ME AAPKA SWAGAT HAI",bg='black',fg='red')
    chat_1.config(font = ("Times New Roman",23))

    b.title('BIHAR')

    
    button = tk.Button(b,text="QUIT",bg='black',fg='red',width=25,activebackground='black',activeforeground='medium orchid',command=b.destroy)
    btn1 = Button(b,text="GAYA",bg='black', fg='red',font=('Courier',20,'bold'),activebackground='black',activeforeground='medium orchid', command=Gaya)
    btn1.place(relx=0.01,rely=0.78, relwidth=0.15,relheight=0.1)
        
    btn2 = Button(b,text="BODH GAYA",bg='black', fg='red',font=('Courier',20,'bold'),activebackground='black',activeforeground='medium orchid', command=b.destroy)
    btn2.place(relx=0.20,rely=0.78, relwidth=0.15,relheight=0.1)
        
    btn3 = Button(b,text="SITAMANI",bg='black', fg='red',font=('Courier',20,'bold'),activebackground='black',activeforeground='medium orchid', command=b.destroy)
    btn3.place(relx=0.40,rely=0.78,relwidth=0.15,relheight=0.1)
        
    btn4 = Button(b,text="PATNA",bg='black', fg='red',font=('Courier',20,'bold'),activebackground='black',activeforeground='medium orchid', command = b.destroy)
    btn4.place(relx=0.60,rely=0.78, relwidth=0.15,relheight=0.1)
        
    btn5 = Button(b,text="NALANDA",bg='black', fg='red',font=('Courier',20,'bold'),activebackground='black',activeforeground='medium orchid', command = b.destroy)
    btn5.place(relx=0.80,rely=0.78, relwidth=0.15,relheight=0.1)

    btn5 = Button(b,text="DARBHANGA",bg='black', fg='red',font=('Courier',20,'bold'),activebackground='black',activeforeground='medium orchid', command = b.destroy)
    btn5.place(relx=1.0,rely=0.78, relwidth=0.15,relheight=0.1)

    #btn6 = Button(b,text="RAJGIR",bg='snow2', fg='red',font=('Courier',20),activebackground='black',activeforeground='medium orchid', command = b.destroy)
    #btn6.place(relx=0.82,rely=0.12, relwidth=0.15,relheight=0.1)



    #btn8 = Button(b,text="Search Reader",bg='black', fg='white', font=('Courier',20),command = b.destroy)
    #btn8.place(relx=0.35,rely=0.80, relwidth=0.35,relheight=0.1)

    #btn9 = Button(b,text="Delete Reader",bg='black', fg='white', font=('Courier',20),command = b.destroy)
    #btn9.place(relx=0.40,rely=0.90, relwidth=0.35,relheight=0.1)

    #btn10 = Button(b,text="QUIT",bg='black', fg='white', font=('Courier',20),command = b.destroy)
    #btn10.place(relx=0.45,rely=1.00, relwidth=0.35,relheight=0.1)

    button.pack()
    button.place(relx=0.86,rely=0.89, relwidth=0.15,relheight=0.05) 
    chat_1.pack()
    chat_1.place(relx=0.68,rely=0.029, relwidth=0.30, relheight=0.08)
    frame_1.pack()
    label_1.pack()
    b.mainloop()


def Main():

    a = tk.Toplevel()

    a.geometry("1800x850")
    frame =Frame(a,width = 1800,height=950)

    frame.place(anchor='center',relx=0.5,rely=0.5)


    img =ImageTk.PhotoImage(Image.open("C:\\Users\\nikhi\\OneDrive\\Desktop\\Tourism\\4.jpg"))

    label = Label(frame,image=img)

    chat = Label(a,text="VACATION VISTA")
    chat.config(font = ("Times New Roman",25))

    a.title('TOURISM')

    


        
    button = tk.Button(a,text="Let's Start the Journey",bg='PeachPuff2',width=25,activebackground='black',activeforeground='medium orchid',command=Start)

    





    button.pack()
    button.place(relx=0.82,rely=0.84, relwidth=0.20,relheight=0.05)
    button_1 = tk.Button(a,text="QUIT",bg='PeachPuff2',width=25,activebackground='black',activeforeground='medium orchid',command=a.destroy)


    
    chat.pack()
    chat.place(relx=0.38,rely=0.029, relwidth=0.20, relheight=0.08)
    frame.pack()
    label.pack()
    button_1.pack()
    button_1.place(relx=0.82,rely=0.89, relwidth=0.20,relheight=0.05)
    a.mainloop()
    

    






Main()


