from tkinter import *
import pymysql
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
 conn = pymysql.connect(host="localhost" , user = "root", passwd =
"jainhimanshu", db = "Form3")
 with conn:
 cursor = conn.cursor()
 cursor.execute('CREATE TABLE IF NOT EXISTS Enroll (intake INT,name
TEXT,type TEXT,procode TEXT,ratio TEXT,diversity TEXT)')
 cursor.execute('INSERT INTO Enroll
(intake,name,type,procode,ratio,diversity)
VALUES(%s,%s,%s,%s,%s,%s)', (intake, name, type1, procode, ratio,
diversity))
 conn.commit()

def delete():
 conn = pymysql.connect(host="localhost" , user="root", passwd =
"jainhimanshu", db = "Form5")
