import os
import sqlite3 as s
import sys
from tkinter import *
from tkinter import ttk
from PIL import ImageTk, Image

# def resource_path(relative_path):
   
#     try:
#         # PyInstaller creates a temp folder and stores path in _MEIPASS
#         base_path = sys._MEIPASS
#     except Exception:
#         base_path = os.path.abspath(".")

#     return os.path.join(base_path, relative_path)
root=Tk()
root.geometry("500x590")
root.title("Entry")
root.configure(background="blue")
frame=Frame(root,borderwidth=5,relief="solid")
frame.pack(fill="both")


path1="21.jpg"
img1 = ImageTk.PhotoImage(Image.open(path1))
bag=Label(frame,image=img1)
bag.place(x=0,y=0,relheight=1,relwidth=1)

#icon
conn = s.connect('new3.db')
c=conn.cursor()
title=Label(frame,text="Noakhali Zilla School Science Club ",font=("Times New Roman",20),bg="#daeff7")
title.pack(padx=0,pady=0)

path = "Logo-modified.ico"
img = ImageTk.PhotoImage(Image.open(path))

panel = Label(frame, image = img,borderwidth=0,bg="#daeff7",relief="solid")
panel.pack()


#setting bg

#...
name=Entry(frame,fg="black",width=30)
name.insert(0,"Name: ")
entry=Entry(frame,fg='black',width=30)
entry.insert(0,"Phone no: ")
opt1=["Noakhali Zilla School","Noakhali Govt. Girls High School","Horinarayanpur High School","Maijdee Balika Biddaniketon","M.A. Rashid High School","Al Faruq Academy"]
opt2=["Junior Math","Junior Science","Senior Math","Senior Science","IQ Test","Team Quiz"]

clicked=StringVar()
clicked.set('School')
drp=OptionMenu(frame,clicked, *opt1)
drp.config(width=25)
#....
clicked1=StringVar()
clicked1.set('Catagory1')
drp1=OptionMenu(frame,clicked1, *opt2)
drp1.config(width=25)
#...
clicked2=StringVar()
clicked2.set('Catagory2')
drp2=OptionMenu(frame,clicked2, *opt2,)
drp2.config(width=25)
#...
clicked3=StringVar()
clicked3.set('Catagory3')
drp3=OptionMenu(frame,clicked3, *opt2,)
drp3.config(width=25)
#..
def insert():
    global d
    a=c.execute("select * from data_entryP where School=?",(clicked.get(),))
    b=1
    for i in a:
        b+=1
    if clicked.get()=="Noakhali Zilla School":
        entry_b=str(1000+b)
    if clicked.get()=="Noakhali Govt. Girls High School":
        entry_b=str(2000+b)
    if clicked.get()=="Horinarayanpur High School":
        entry_b=str(3000+b)
    if clicked.get()=="Maijdee Balika Biddaniketon":
        entry_b=str(4000+b)
    if clicked.get()=="M.A. Rashid High School":
        entry_b=str(5000+b)
    if clicked.get()=="Al Faruq Academy":
        entry_b=str(6000+b)
    catagory=f"1) {clicked1.get()} 2) {clicked2.get()} 3) {clicked3.get()}"
    d=[(name.get().replace("Name: ","").capitalize(),entry.get().replace("Phone no: ",""),clicked.get(),catagory,0,entry_b)]
    c.executemany("insert into data_entryP(name,Phone_no,School,Catagory,Marks,Entry_no) values(?,?,?,?,?,?)",d)
    name.delete(6,"end")
    entry.delete(10,"end")

    clicked.set("School")
    clicked1.set("Catagory")
    clicked2.set("Catagory")
    clicked3.set("Catagory")

    
        
    
#/.////////././//// also the code for adding scrollbar
def show():  
    global datas
    datas=c.execute("select * from data_entryP")
    black=Tk()
    black.geometry("1650x700")
    #creating frame
    mainframe=Frame(black)
    mainframe.pack(fill=BOTH,expand=1)
    #creating canvas
    canvas=Canvas(mainframe)
    canvas.pack(side=LEFT,fill=BOTH,expand=1)
    #adding scroll
    scrollbar=ttk.Scrollbar(mainframe,orient=VERTICAL,command=canvas.yview)
    scrollbar.pack(side=RIGHT,fill=Y)
    #config
    canvas.configure(yscrollcommand=scrollbar.set)
    canvas.bind("<Configure>",lambda e: canvas.configure(scrollregion=canvas.bbox("all")))
    #adding new feame
    frame2=Frame(canvas,relief="solid",pady=5,padx=5)
    canvas.create_window((0,0), window=frame2,anchor="nw")
    b=1
    #Main loop
    for i in datas:
        
        textbox=Label(frame2,text=f"Name: {i[0]}",relief="solid",width=40,height=2,background="light blue")
        textbox.grid(row=b+1,column=1,padx=5)
        t2=Label(frame2,text=f"Phone_no: {i[1]}",relief="solid",width=30,height=2)
        t2.grid(row=b+1,column=2)
        t3=Label(frame2,text=f"School: {i[2]}",relief="solid",width=50,height=2,background="light yellow")
        t3.grid(row=b+1,column=3)
        t4=Label(frame2,text=f"Catagory: {i[3]}",relief="solid",width=50,height=2)
        t4.grid(row=b+1,column=4)
        al=Label(frame2,text=f"Entry no: {i[4]}",relief="solid",width=20,height=2,background="light green")
        al.grid(row=b+1,column=5,pady=3)
        
        

        #...
        def selected(event):
            exe=f"select * from data_entryP where Catagory like '%{clicked.get()}%'"
            a=c.execute(exe)
            new=Tk()
            new.geometry("1650x700")
            new.title(clicked.get())
            b=1
            mainframe=Frame(new)
            mainframe.pack(fill=BOTH,expand=1)
    #creating canvas
            canvas=Canvas(mainframe)
            canvas.pack(side=LEFT,fill=BOTH,expand=1)
    #adding scroll
            scrollbar=ttk.Scrollbar(mainframe,orient=VERTICAL,command=canvas.yview)
            scrollbar.pack(side=RIGHT,fill=Y)
    #config
            canvas.configure(yscrollcommand=scrollbar.set)
            canvas.bind("<Configure>",lambda e: canvas.configure(scrollregion=canvas.bbox("all")))
    #adding new feame
            frame2=Frame(canvas)
            canvas.create_window((0,0), window=frame2,anchor="nw")
            for i in a:
                
                textbox=Label(frame2,text=f"Name: {i[0]}",relief="solid",width=40,height=2)
                textbox.grid(row=b,column=1)
                t2=Label(frame2,text=f"Mobile: {i[1]}",relief="solid",width=30,height=2)
                t2.grid(row=b,column=2)
                t3=Label(frame2,text=f"School: {i[2]}",relief="solid",width=50,height=2)
                t3.grid(row=b,column=3)
                t4=Label(frame2,text=f"Catagory: {i[3]}",relief="solid",width=50,height=2)
                t4.grid(row=b,column=4)
                t5=Label(frame2,text=f"Entry No: {i[4]}",relief="solid",width=30,height=2)
                t5.grid(row=b,column=5)
                
                b+=1
            new.mainloop()
        def show_d(event):
            nam=S_E.get()
            data=c.execute("select * from data_entryP where name=?",(nam.capitalize(),))
            show_win=Tk()
            # str1=50*len(data.fetchall())
            # text=f"1650x{str1}"
            show_win.geometry(f"1650x100")
            b=1
            for i in data:
                textbox=Label(show_win,text=f"Name: {i[0]}",relief="solid",width=40,height=2)
                textbox.grid(row=b,column=1)
                t2=Label(show_win,text=f"Mobile: {i[1]}",relief="solid",width=30,height=2)
                t2.grid(row=b,column=2)
                t3=Label(show_win,text=f"School: {i[2]}",relief="solid",width=50,height=2)
                t3.grid(row=b,column=3)
                t4=Label(show_win,text=f"Catagory: {i[3]}",relief="solid",width=50,height=2)
                t4.grid(row=b,column=4)
                t5=Label(show_win,text=f"Entry No: {i[4]}",relief="solid",width=30,height=2)
                t5.grid(row=b,column=5)
                b+=1
            show_win.mainloop()
        def show_d1(event):
            nam=S_A.get()
            show_win=Tk()
            show_win.geometry("1620x50")
            data=c.execute("select * from data_entryP where Entry_no=?",(nam,))
            b=1
            for i in data:
                textbox=Label(show_win,text=f"Name: {i[0]}",relief="solid",width=40,height=2)
                textbox.grid(row=b,column=1)
                t2=Label(show_win,text=f"Mobile: {i[1]}",relief="solid",width=30,height=2)
                t2.grid(row=b,column=2)
                t3=Label(show_win,text=f"School: {i[2]}",relief="solid",width=50,height=2)
                t3.grid(row=b,column=3)
                t4=Label(show_win,text=f"Catagory: {i[3]}",relief="solid",width=50,height=2)
                t4.grid(row=b,column=4)
                t5=Label(show_win,text=f"Entry No: {i[4]}",relief="solid",width=30,height=2)
                t5.grid(row=b,column=5)
                b+=1
            show_win.mainloop()
        opt=["Junior Math","Junior Science","Senior Math","Senior Science","Team Quiz","IQ Test"]
        clicked=StringVar()
        clicked.set('Sort')
        drp=OptionMenu(frame2,clicked, *opt,command=selected)
        drp.grid(row=2,column=7,padx=5)
        Search=Label(frame2,width=5,text="Search:",fg="black")
        Search.grid(row=1,column=1)       
        S_E=Entry(frame2,width=5,text="Search:",fg="black",relief="solid") 
        S_E.config(width=30)
        S_E.bind('<Return>',show_d)
        S_E.grid(row=1,column=2)
        S_A=Entry(frame2,width=5,text="Search:",fg="black",relief="solid") 
        S_A.config(width=30)
        S_A.bind('<Return>',show_d1)
        S_A.grid(row=1,column=3)

        #Insert function for the button
        b+=1
    black.title("Database")
    black.mainloop()
    
#Delete
def delete():
    delete=Tk()
    delete.title("Delete Entry")
    delete.geometry("300x100")
    entr=Entry(delete)
    entr.pack()
    entr1=Entry(delete)
    entr1.pack()
    def main_delete():
        if entr.get()=="" and entr1.get()=="":
            delete.destroy()
        elif entr.get()!="" and entr1.get()=="":
            num=entr.get()
            execute=f"DELETE from data_entryP where Entry_no = {num}"
            c.execute(execute)
            delete.destroy()
        elif entr.get()=="" and entr1.get()!="":    
            name1=entr1.get()
            execute1=f"DELETE from data_entryP where name = '{name1}'"
            c.execute(execute1)
            delete.destroy()
    ok=Button(delete,text="ok",command=main_delete)
    ok.pack()
    
    delete.mainloop()



button=Button(frame,text="Insert",command=insert)
button.pack(pady=10)


name.pack()
entry.pack()
drp.pack()
drp1.pack()
drp2.pack()
drp3.pack()
command=Button(frame,fg="black",text="Show",command=show)
command.pack()
delete1=Button(frame,fg="black",text="Delete",command=delete)
delete1.pack()
a=Label(frame,fg="black",text="Delete")
a.pack(pady=230)
print("Executed Successfully")
root.mainloop()
conn.commit() 