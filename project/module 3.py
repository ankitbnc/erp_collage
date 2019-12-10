from tkinter import *
import sqlite3
root = Tk()
root.geometry('550x600')
root.title("Student Enrollment")
c1 = StringVar()
c2 = StringVar()
c3 = StringVar()
c4 = StringVar()
c5 = StringVar()
c6 = StringVar()
def database():
 intake = c1.get()
 name = c2.get()
 type1 = c3.get()
 procode = c4.get()
 ratio = c5.get()
 diversity = c6.get()
 conn = sqlite3.connect('Form3.db')
 with conn:
    cursor = conn.cursor()
    cursor.execute('CREATE TABLE IF NOT EXISTS Enroll (intake INT,name TEXT,type TEXT,procode TEXT,ratio TEXT,diversity TEXT)')
    cursor.execute('INSERT INTO Enroll(intake,name,type,procode,ratio,diversity)VALUES(%s,%s,%s,%s,%s,%s)', (intake, name, type1, procode, ratio,diversity))
    conn.commit()

def delete():
    conn = sqlite3.connect('Form3.db')
    c = conn.cursor()
    c.execute("DELETE from Enroll")
    conn.commit()


label_0 = Label(root, text = "Student Enrollment", width = 20, font =
("bold", 30))
label_0.place(x=90, y=50)
label_1 = Label(root, text="Intake of the Program", width=20,
font=("bold", 10))
label_1.place(x=70, y=130)
entry_1 = Entry(root, textvar=c1)
entry_1.place(x=240, y=130)
label_2 = Label(root, text="Name of the Program", width=20, font=("bold",
10))
label_2.place(x=70, y=180)
list2 = ['B.Tech', 'B.Des', 'M.Tech', 'MBA', 'LLB', 'BCA', 'PhD', 'BBA',
'B.Pharma'];
droplist = OptionMenu(root, c2, *list2)
droplist.config(width=20)
c2.set('Select your Program')
droplist.place(x=230, y=180)
label_3 = Label(root, text="Type of the Program", width=20, font=("bold",
10))
label_3.place(x=70, y=230)
list3 = ['CSE', 'Non-CSE', 'Management', 'Designing', 'Law', 'Health
Care'];
droplist = OptionMenu(root, c3, *list3)
droplist.config(width=20)
c3.set('Select your Program')
droplist.place(x=230, y=230)
label_4 = Label(root, text="Program Code", width=20, font=("bold", 10))
label_4.place(x=70, y=280)
entry_4 = Entry(root, textvar=c4)
entry_4.place(x=240, y=280)
label_5 = Label(root, text="Male/Female Ratio", width=20, font=("bold",
10))
label_5.place(x=70, y=330)
entry_5 = Entry(root, textvar=c5)
entry_5.place(x=240, y=330)
label_6 = Label(root, text="Diversity (Region Wise)", width=20,
font=("bold", 10))
label_6.place(x=70, y=380)
entry_6 = Entry(root, textvar=c6)
entry_6.place(x=240, y=380)
Button(root, text='Delete', width=20, bg='White', fg='Black',
command=delete).place(x=180, y=430)
Button(root, text='Submit', width=20, bg='White', fg='Black',
command=database).place(x=180, y=480)
root.mainloop()