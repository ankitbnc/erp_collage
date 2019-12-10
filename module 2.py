from tkinter import *
import sqlite3

root = Tk()
root.geometry('600x600')
root.title("Research Details")

c1 = StringVar()
c2 = StringVar()
c3 = StringVar()
c4 = StringVar()
c5 = StringVar()
c6 = IntVar()
c7 = IntVar()
c8 = IntVar()
c9 = StringVar()
c10 = StringVar()

var1 = IntVar()


def database():
    sno = c1.get()
    nameofproject = c2.get()
    investigator = c3.get()
    fundingagency = c4.get()
    type = var1.get()
    department = c5.get()
    yearofaward = c6.get()
    funds = c7.get()
    duration = c8.get()
    linkofsanctioned = c9.get()
    linkofutilization = c10.get()
    conn = sqlite3.connect('Form2.db')
    with conn:
        cursor = conn.cursor()
    cursor.execute(
        'CREATE TABLE IF NOT EXISTS Research (sno INTEGER,nameofproject TEXT,investigator TEXT,fundingagency TEXT,type TEXT, department TEXT, yearofaward INTEGER, funds INTEGER, duration INTEGER, linkofsanctioned TEXT, linkofutilization TEXT)')
    cursor.execute(
        'INSERT INTO Research (sno,nameofproject,investigator,fundingagency,type, department, yearofaward, funds, duration, linkofsanctioned, linkofutilization) VALUES(?,?,?,?,?,?,?,?,?,?,?)',
        (sno, nameofproject, investigator, fundingagency, type, department, yearofaward, funds, duration,
         linkofsanctioned, linkofutilization))
    conn.commit()


def delete():
    conn = sqlite3.connect('Form2.db')
    c = conn.cursor()
    c.execute("DELETE from Research")

    conn.commit()


label_0 = Label(root, text="Research Details", width=20, font=("bold", 20))
label_0.place(x=200, y=40)

label_1 = Label(root, text="Serial No", width=20, font=("bold", 10))
label_1.place(x=180, y=100)

entry_1 = Entry(root, textvar=c1)
entry_1.place(x=340, y=100)

label_2 = Label(root, text="Project Name", width=20, font=("bold", 10))
label_2.place(x=180, y=130)

entry_2 = Entry(root, textvar=c2)
entry_2.place(x=340, y=130)

label_3 = Label(root, text="Investigator Name", width=20, font=("bold", 10))
label_3.place(x=180, y=160)

entry_3 = Entry(root, textvar=c3)
entry_3.place(x=340, y=160)

label_4 = Label(root, text="Funding Agency", width=20, font=("bold", 10))
label_4.place(x=180, y=190)

entry_4 = Entry(root, textvar=c4)
entry_4.place(x=340, y=190)

label_5 = Label(root, text="Type", width=20, font=("bold", 10))
label_5.place(x=180, y=220)
var2 = IntVar()
Checkbutton(root, text="Government", variable=var1).place(x=340, y=220)
Checkbutton(root, text="Non-Government", variable=var2).place(x=440, y=220)

label_6 = Label(root, text="Department of Investigator", width=20, font=("bold", 10))
label_6.place(x=180, y=250)

entry_6 = Entry(root, textvar=c5)
entry_6.place(x=340, y=250)

label_7 = Label(root, text="Year of Award", width=20, font=("bold", 10))
label_7.place(x=180, y=280)

entry_7 = Entry(root, textvar=c6)
entry_7.place(x=340, y=280)

label_8 = Label(root, text="Funds Provided (INR in lakhs)", width=20, font=("bold", 10))
label_8.place(x=180, y=310)

entry_8 = Entry(root, textvar=c7)
entry_8.place(x=340, y=310)

label_9 = Label(root, text="Duration", width=20, font=("bold", 10))
label_9.place(x=180, y=340)

entry_9 = Entry(root, textvar=c8)
entry_9.place(x=340, y=340)

label_10 = Label(root, text="Link of Sanctioned Letter", width=20, font=("bold", 10))
label_10.place(x=180, y=370)

entry_8 = Entry(root, textvar=c9)
entry_8.place(x=340, y=370)

label_9 = Label(root, text="Link of Utalization Certificate", width=20, font=("bold", 10))
label_9.place(x=180, y=400)

entry_9 = Entry(root, textvar=c10)
entry_9.place(x=340, y=400)

Button(root, text='Delete', width=20, bg='white', fg='brown', command=delete).place(x=250, y=450)

Button(root, text='Submit', width=20, bg='black', fg='white', command=database).place(x=250, y=500)

root.mainloop()