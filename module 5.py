from tkinter import *
import sqlite3

root = Tk()
root.geometry('500x500')
root.title("Curriculum")

c1 = StringVar()
c2 = StringVar()
c3 = StringVar()
s1 = StringVar()
var1 = IntVar()


def database():
    name = c1.get()
    type = c2.get()
    code = c3.get()
    spec = s1.get()
    revised = var1.get()
    conn = sqlite3.connect('Form5.db')
    with conn:
        cursor = conn.cursor()
    cursor.execute('CREATE TABLE IF NOT EXISTS Student (name TEXT,type TEXT,code TEXT,spec TEXT,revised TEXT)')
    cursor.execute('INSERT INTO Student (name,type,code,spec,revised) VALUES(?,?,?,?,?)',
                   (name, type, code, spec, revised,))
    conn.commit()


def delete():
    conn = sqlite3.connect('Form5.db')
    c = conn.cursor()
    c.execute("DELETE from Student")

    conn.commit()


label_0 = Label(root, text="Curriculum", width=20, font=("bold", 20))
label_0.place(x=90, y=50)

label_1 = Label(root, text="Name of the Program", width=20, font=("bold", 10))
label_1.place(x=70, y=130)

list1 = ['B.Tech', 'B.Des', 'M.Tech', 'MBA', 'LLB', 'BCA', 'PhD', 'BBA', 'B.Pharma'];

droplist = OptionMenu(root, c1, *list1)
droplist.config(width=20)
c1.set('Select your Program')
droplist.place(x=240, y=130)

label_2 = Label(root, text="Type of the Program", width=20, font=("bold", 10))
label_2.place(x=70, y=180)

list2 = ['CSE', 'Non-CSE', 'Management', 'Designing', 'Law', 'Health Care'];

droplist = OptionMenu(root, c2, *list2)
droplist.config(width=20)
c2.set('Select your Program')
droplist.place(x=240, y=180)

label_3 = Label(root, text="Program Code", width=20, font=("bold", 10))
label_3.place(x=70, y=230)

entry_3 = Entry(root, textvar=c3)
entry_3.place(x=240, y=230)

label_4 = Label(root, text="Specialization", width=20, font=("bold", 10))
label_4.place(x=70, y=280)

entry_4 = Entry(root, textvar=s1)
entry_4.place(x=240, y=280)

label_5 = Label(root, text="Revised Program", width=20, font=("bold", 10))
label_5.place(x=70, y=330)
var2 = IntVar()
Checkbutton(root, text="Yes", variable=var1).place(x=240, y=330)
Checkbutton(root, text="No", variable=var2).place(x=290, y=330)

Button(root, text='Delete', width=20, bg='White', fg='Brown', command=delete).place(x=180, y=380)

Button(root, text='Submit', width=20, bg='black', fg='white', command=database).place(x=180, y=440)

root.mainloop()