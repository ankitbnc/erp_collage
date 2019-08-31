from tkinter import *
import sqlite3

root = Tk()
root.geometry('1130x500')
root.title("Placement Internship Details")


c1=StringVar()
c2=StringVar()
c3=StringVar()
c4=IntVar()
c5=StringVar()
c6=StringVar()
c7=StringVar()
c8=StringVar()
c9=StringVar()
c10=StringVar()
c11=StringVar()
c12=StringVar()
c13=StringVar()
c14=StringVar()
c15=StringVar()
c16=StringVar()
c17=StringVar()
c18=StringVar()
c19=StringVar()
c20=StringVar()

var1= IntVar()
var3= IntVar()
var5=IntVar()
var7=IntVar()

def database():
   nameofPIC=c1.get()
   nameofstudent=c2.get()
   course=c3.get()
   SAPID=c4.get()
   RollNo=c5.get()
   interncompany=c6.get()
   optforplacement=var3.get()
   placedcompany=c7.get()
   internship=var1.get()
   placementrecieved=var5.get()
   nameofCC=c8.get()
   certificationDone=c9.get()
   achievements=c10.get()
   nameofAC=c11.get()
   IV_visited=var7.get()
   IVlocation=c12.get()
   minor1=c13.get()
   mentor1=c14.get()
   minor2=c15.get()
   mentor2=c16.get()
   major1=c17.get()
   mentormajor1=c18.get()
   major2=c19.get()
   mentormajor2=c20.get()
   
   
   conn = sqlite3.connect('Form8.db')
   with conn:
      cursor=conn.cursor()
   cursor.execute('CREATE TABLE IF NOT EXISTS PIC (nameofPIC TEXT,nameofstudent TEXT,course TEXT,SAPID INTEGER,RollNo TEXT, internship TEXT, interncompany TEXT, optforplacement TEXT, placementrecieved TEXT, placedcompany TEXT)')
   cursor.execute('CREATE TABLE IF NOT EXISTS CC (nameofCC TEXT,nameofstudent TEXT,certificationDone TEXT, Achievements TEXT)')
   cursor.execute('CREATE TABLE IF NOT EXISTS AC (nameofAC TEXT,nameofstudent TEXT,IV_visited TEXT,IVlocation TEXT,minor1 TEXT, mentor1 TEXT, minor2 TEXT, mentor2 TEXT, major1 TEXT, mentormajor1 TEXT, major2 TEXT, mentormajor2 TEXT)')
   cursor.execute('INSERT INTO PIC (nameofPIC,nameofstudent,course,SAPID,RollNo,internship, interncompany, optforplacement, placementrecieved, placedcompany ) VALUES(?,?,?,?,?,?,?,?,?,?)',(nameofPIC,nameofstudent,course,SAPID,RollNo,internship,interncompany,optforplacement,placementrecieved,placedcompany))
   cursor.execute('INSERT INTO CC (nameofCC,nameofstudent,certificationDone, Achievements ) VALUES(?,?,?,?)',(nameofCC,nameofstudent,certificationDone,achievements))
   cursor.execute('INSERT INTO AC (nameofAC,nameofstudent,IV_visited,IVlocation,minor1, mentor1, minor2, mentor2, major1, mentormajor1, major2, mentormajor2) VALUES(?,?,?,?,?,?,?,?,?,?,?,?)',(nameofAC,nameofstudent,IV_visited,IVlocation,minor1, mentor1, minor2, mentor2, major1, mentormajor1, major2, mentormajor2))
   conn.commit()
   
def delete1():
    conn = sqlite3.connect('Form8.db')
    c = conn.cursor()
    c.execute("DELETE from PIC")

    conn.commit()

def delete2():
    conn = sqlite3.connect('Form8.db')
    c = conn.cursor()
    c.execute("DELETE from CC")

    conn.commit()

def delete3():
    conn = sqlite3.connect('Form8.db')
    c = conn.cursor()
    c.execute("DELETE from AC")

    conn.commit()
             
label_0 = Label(root, text="PIC Details",width=20,font=("bold", 20))
label_0.place(x=90,y=50)


label_1 = Label(root, text="Name of the PIC",width=20,font=("bold", 10))
label_1.place(x=80,y=100)

entry_1 = Entry(root,textvar=c1)
entry_1.place(x=240,y=100)

label_2 = Label(root, text="Name of the Student",width=20,font=("bold", 10))
label_2.place(x=80,y=130)

entry_2 = Entry(root,textvar=c2)
entry_2.place(x=240,y=130)

label_3 = Label(root, text="Course",width=20,font=("bold", 10))
label_3.place(x=80,y=160)

entry_3 = Entry(root,textvar=c3)
entry_3.place(x=240,y=160)   

label_4 = Label(root, text="SAP ID",width=20,font=("bold", 10))
label_4.place(x=80,y=190)

entry_4 = Entry(root,textvar=c4)
entry_4.place(x=240,y=190)


label_5 = Label(root, text="Roll No",width=20,font=("bold", 10))
label_5.place(x=80,y=220)

entry_5 = Entry(root,textvar=c5)
entry_5.place(x=240,y=220)

label_6= Label(root, text="Internship Done",width=20,font=("bold", 10))
label_6.place(x=80,y=250)
var2= IntVar()
Checkbutton(root, text="Yes", variable=var1).place(x=240,y=250)
Checkbutton(root, text="No", variable=var2).place(x=290,y=250)

label_7 = Label(root, text="Internship Company Name",width=20,font=("bold", 10))
label_7.place(x=80,y=280)

entry_7 = Entry(root,textvar=c6)
entry_7.place(x=240,y=280)

label_8= Label(root, text="Opt for Placement Process",width=20,font=("bold", 10))
label_8.place(x=80,y=310)
var4= IntVar()
Checkbutton(root, text="Yes", variable=var3).place(x=240,y=310)
Checkbutton(root, text="No", variable=var4).place(x=290,y=310)

label_9 = Label(root, text="Placement Recieved",width=20,font=("bold", 10))
label_9.place(x=80,y=340)
var6= IntVar()
Checkbutton(root, text="Yes", variable=var5).place(x=240,y=340)
Checkbutton(root, text="No", variable=var6).place(x=290,y=340)


label_10 = Label(root, text="Placed Company Name",width=20,font=("bold", 10))
label_10.place(x=80,y=370)

entry_10= Entry(root,textvar=c7)
entry_10.place(x=240,y=370)

Button(root, text='Delete',width=20,bg='White',fg='Brown',command=delete1).place(x=170,y=400)


label_01 = Label(root, text="CC Details",width=20,font=("bold", 20))
label_01.place(x=500,y=50)

label_11 = Label(root, text="Name of the CC",width=20,font=("bold", 10))
label_11.place(x=480,y=100)

entry_11= Entry(root,textvar=c8)
entry_11.place(x=640,y=100)


label_13 = Label(root, text="Certifications (if any)",width=20,font=("bold", 10))
label_13.place(x=480,y=130)

entry_13= Entry(root,textvar=c9)
entry_13.place(x=640,y=130)

label_14 = Label(root, text="Achievements (if Any)",width=20,font=("bold", 10))
label_14.place(x=480,y=160)

entry_14= Entry(root,textvar=c10)
entry_14.place(x=640,y=160)

Button(root, text='Delete',width=20,bg='White',fg='Brown',command=delete2).place(x=580,y=200)


label_02 = Label(root, text="AC Details",width=20,font=("bold", 20))
label_02.place(x=900,y=50)


label_15 = Label(root, text="Name of the AC",width=20,font=("bold", 10))
label_15.place(x=880,y=100)

entry_15 = Entry(root,textvar=c11)
entry_15.place(x=1040,y=100)

label_16= Label(root, text="IV Visited",width=20,font=("bold", 10))
label_16.place(x=880,y=130)
var8= IntVar()
Checkbutton(root, text="Yes", variable=var7).place(x=1040,y=130)
Checkbutton(root, text="No", variable=var8).place(x=1090,y=130)


label_17 = Label(root, text="IV Location",width=20,font=("bold", 10))
label_17.place(x=880,y=160)

entry_17 = Entry(root,textvar=c12)
entry_17.place(x=1040,y=160)   

label_18 = Label(root, text="Minor 1 Title",width=20,font=("bold", 10))
label_18.place(x=880,y=190)

entry_18 = Entry(root,textvar=c13)
entry_18.place(x=1040,y=190)


label_19 = Label(root, text="Minor 1 Mentor",width=20,font=("bold", 10))
label_19.place(x=880,y=220)

entry_19 = Entry(root,textvar=c14)
entry_19.place(x=1040,y=220)


label_20 = Label(root, text="Minor 2 Title",width=20,font=("bold", 10))
label_20.place(x=880,y=250)

entry_21 = Entry(root,textvar=c15)
entry_21.place(x=1040,y=250)


label_22 = Label(root, text="Minor 2 Mentor",width=20,font=("bold", 10))
label_22.place(x=880,y=280)

entry_22= Entry(root,textvar=c16)
entry_22.place(x=1040,y=280)


label_23 = Label(root, text="Major 1 Title",width=20,font=("bold", 10))
label_23.place(x=880,y=310)

entry_24= Entry(root,textvar=c17)
entry_24.place(x=1040,y=310)

label_25 = Label(root, text="Major 1 Mentor",width=20,font=("bold", 10))
label_25.place(x=880,y=340)

entry_25= Entry(root,textvar=c18)
entry_25.place(x=1040,y=340)

label_26 = Label(root, text="Major 2 Title",width=20,font=("bold", 10))
label_26.place(x=880,y=370)

entry_27= Entry(root,textvar=c19)
entry_27.place(x=1040,y=370)

label_28 = Label(root, text="Major 2 Mentor",width=20,font=("bold", 10))
label_28.place(x=880,y=400)

entry_29 = Entry(root,textvar=c20)
entry_29.place(x=1040,y=400)

Button(root, text='Delete',width=20,bg='White',fg='Brown',command=delete3).place(x=980,y=430)


Button(root, text='Submit',width=20,bg='Black',fg='white',command=database).place(x=565,y=480)


root.mainloop()
