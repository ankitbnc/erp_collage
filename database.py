#ERP PROGRAM BY AAKASH SIROHI
from tkinter import *
from PIL import ImageTk,Image
import sqlite3

root=Tk()
root.title('University ERP System')
the_label = Label(root,text="RESEARCH DETAILS")
the_label.grid()
the_label2= Label(root,text="CURRICULUM => Board of Studies" )
the_label2.grid(row=13)
the_label4= Label(root, text = "PIC DETAILS")
the_label4.grid(row=22)
the_label5= Label(root, text = "ACTIVITY COORDINATOR DETAILS")
the_label5.grid(row=0, column=4)
the_label6= Label(root, text = "COURSE COORDINATOR DETAILS")
the_label6.grid(row=46)
root.geometry("1600x1200")

#CONNECTING TO A DATABASE
conn = sqlite3.connect('college_database2.db')
# CREATE CURSOR
c = conn.cursor()
vary=IntVar()
varn=IntVar()



#CREATE TABLE IN DATABASE(this execute command is commented out because this has already executed on my side)

'''
c.execute("""CREATE TABLE research_details(

        s_no text,
        name_of_project text,
        name_of_co_inv text,
        name_of_funding_ag text,
        type text,
        dept_of_co_inv text,
        year integer,
        funds_provided integer,
        duration integer,
        link1 text,
        link2 text
        )""")
c.execute("""CREATE TABLE board_of_studies(
        name_of_program text,
        type_of_program text,
        program_code integer,
        specialisation text,
        revised_course text)""")
c.execute("""CREATE TABLE pic_details(
        name_of_pic text,
        name_of_stu text,
        course text,
        sap_id integer,
        roll_no integer,
        internship_done text,
        internship_company_name text,
        opt_for_placement_program text,
        placement_received text,
        placed_company_name text
)""")
c.execute("""CREATE TABLE activity_coordinator_details(
        ac_name text,
        student_name text,
        iv_visited text,
        location_for_iv text,
        minor1_project_name text,
        minor1_mentor text,
        minor2_project_name text,
        minor2_mentor text,
        major1_project_name text,
        major1_mentor text,
        major2_project_name text,
        major2_mentor text
)""")

c.execute("""CREATE TABLE course_coordinator_details(
        cc_name text,
        name_of_student text,
        certification_done text,
        achievements text)""")
'''
#CREATE SUBMIT FUNCTION
def submit():
    # DATABASES
    #CONNECTING TO DATABASE
    conn = sqlite3.connect('college_database.db')

    # CREATE CURSOR INSIDE SUBMIT FUNCTION
    c = conn.cursor()
    # commit changes
    #INSERT INTO TABLE
    c.execute("INSERT INTO research_details VALUES (:s_no,:name_of_project,:name_of_principal,:name_of_funding_ag,:type ,:dept_of_co_inv ,:year ,:funds_provided,:duration ,:link1 ,:link2)",

              dict(s_no=s_no.get(), name_of_project=name_of_pro.get(), name_of_principal=co_invst.get(),
                   name_of_funding_ag=name_of_fagency.get(), type=typ.get(), dept_of_co_inv=dep.get(), year=yr.get(),
                   funds_provided=fun.get(), duration=dtn.get(), link1=ln1.get(), link2=ln2.get())),
    c.execute("INSERT INTO board_of_studies VALUES(:name_of_program,:type_of_program,:program_code,:specialisation,:revised_course)",

                dict(name_of_program = name_prog.get(),type_of_program=type_prog.get(),program_code=prog_code.get(), specialisation=spe.get(),revised_course=rev_cour.get()

              ))
    c.execute("INSERT INTO pic_details VALUES(:name_of_pic,:name_of_stu,:course,:sap_id,:roll_no,:internship_done,:internship_company_name,:opt_for_placement_program,:placement_received,:placed_company_name)",

                dict(name_of_pic=name_pic.get(),name_of_stu=name_stu.get(),course=cour.get(),sap_id=sapid.get(),roll_no=rollno.get(),internship_done=int_done.get(),internship_company_name=int_company_name.get(),opt_for_placement_program=opt_placement_program.get(),placement_received=pla_received.get(),
                     placed_company_name=pla_company_name.get()
                ))


    c.execute("INSERT INTO activity_coordinator_details VALUES(:ac_name,:student_name, :iv_visited,:location_for_iv,:minor1_project_name,:minor1_mentor,:minor2_project_name,:minor2_mentor,:major1_project_name,:major1_mentor,:major2_project_name,:major2_mentor)",
              dict(ac_name=acname.get(), student_name=stu_name.get(), iv_visited=iv_vis.get(),
                   location_for_iv=loc_for_iv.get(), minor1_project_name=mi1_project_name.get(),
                   minor1_mentor=mi1_mentor.get(), minor2_project_name=mi2_project_name.get(),
                   minor2_mentor=mi2_mentor.get(), major1_project_name=ma1_project_name.get(),
                   major1_mentor=ma1_mentor.get(), major2_project_name=ma2_project_name.get(),
                   major2_mentor=ma2_mentor.get())
              )

    #commit connection
    conn.commit()
    # close connection
    conn.close()
    #CLEAR THE TEXT BOXES
    s_no.delete(0,END)
    name_of_pro.delete(0,END)
    co_invst.delete(0,END)
    name_of_fagency.delete(0,END)
    typ.delete(0,END)
    dep.delete(0,END)
    yr.delete(0,END)
    fun.delete(0,END)
    dtn.delete(0,END)
    ln1.delete(0,END)
    ln2.delete(0,END)
    name_prog.delete(0,END)
    type_prog.delete(0,END)
    prog_code.delete(0,END)
    spe.delete(0,END)
    rev_cour.delete(0,END)
    name_pic.delete(0,END)
    name_stu.delete(0,END)
    cour.delete(0,END)
    sapid.delete(0,END)
    rollno.delete(0,END)
    int_done.delete(0,END)
    int_company_name.delete(0,END)
    opt_placement_program.delete(0,END)
    pla_received.delete(0,END)
    pla_company_name.delete(0,END)
    acname.delete(0,END)
    stu_name.delete(0,END)
    iv_vis.delete(0,END)
    loc_for_iv.delete(0,END)
    mi1_project_name.delete(0,END)
    mi1_mentor.delete(0,END)
    mi2_project_name.delete(0,END)
    mi2_mentor.delete(0,END)
    ma1_project_name.delete(0,END)
    ma1_mentor.delete(0,END)
    ma2_project_name.delete(0,END)
    ma2_mentor.delete(0,END)

#DEFINING QUERY FUNCTIOn
def query():
    conn = sqlite3.connect('college_database.db')

    # CREATE CURSOR INSIDE SUBMIT FUNCTION
    c = conn.cursor()
    #CREATING NEW WINDOW TO SHOW RECORDS
    top=Toplevel()
    top.title('STUDENT DATABASE')
    top.geometry("800x800")
    #QUERYING THE DATABASE
    c.execute("SELECT * FROM research_details")
    records=c.fetchall()

    #LOOPING IN RECORDS
    print_records=''
    for record in records:
        print_records +=str(record[0]) + "\n"
    query_label = Label(top, text = print_records)
    query_label.grid(row=0,column=0,columnspan=2)
    '''c.execute("SELECT * FROM board_of_studies")
    c.execute("SELECT * FROM pic_details")
    c.execute("SELECT * FROM activity_coordinator_details")
    c.execute("SELECT * FROM course_coordinator_details")'''
    # COMMIT CONNECTION
    conn.commit()
    # close connection
    conn.close()

#DELETE FUNCTION

def delete():
    conn = sqlite3.connect('college_database.db')
    c = conn.cursor()
    c.execute("DELETE from research_details WHERE OID=PLACEHOLDER")

    conn.commit()
    conn.close()

#CREATING TEXT BOXES
#RESEARCH DETAILS
s_no = Entry(root, width = 50)
s_no.grid(row=1,column=1,padx=0)
name_of_pro= Entry(root, width = 50)
name_of_pro.grid(row=2,column=1)
co_invst= Entry(root, width = 50)
co_invst.grid(row=3,column=1)
name_of_fagency= Entry(root, width = 50)
name_of_fagency.grid(row=4,column=1)
typ=Entry(root,width=50)
typ.grid(row=5,column =1)
dep=Entry(root,width=50)
dep.grid(row=6,column =1)
yr=Entry(root,width=50)
yr.grid(row=7,column =1)
fun=Entry(root,width=50)
fun.grid(row=8,column =1)
dtn=Entry(root,width=50)
dtn.grid(row=9,column =1)
ln1=Entry(root,width=50)
ln1.grid(row=10,column =1)
ln2=Entry(root,width=50)
ln2.grid(row=11,column =1)
#BOARD OF STUDIES
name_prog=Entry(root,width=50)
name_prog.grid(row=14,column =1)
type_prog=Entry(root,width=50)
type_prog.grid(row=15,column =1)
prog_code=Entry(root,width=50)
prog_code.grid(row=16,column =1)
spe=Entry(root,width=50)
spe.grid(row=17,column =1)
rev_cour=Entry(root,width=50)
rev_cour.grid(row=18,column =1)
#PIC_DETAILS
name_pic=Entry(root,width=50)
name_pic.grid(row=21,column =1)
name_stu =Entry(root,width=50)
name_stu .grid(row=22,column =1)
cour=Entry(root,width=50)
cour.grid(row=23,column =1)
sapid=Entry(root,width=50)
sapid.grid(row=24,column =1)
rollno=Entry(root,width=50)
rollno.grid(row=25,column =1)
int_done=Entry(root,width=50)
int_done.grid(row=26,column =1)
int_company_name=Entry(root,width=50)
int_company_name.grid(row=27,column =1)
opt_placement_program=Entry(root,width=50)
opt_placement_program.grid(row=28,column =1)


pla_received=Entry(root,width=50)
pla_received.grid(row=30,column=1)
#pla_received_n.grid(row = 29 , column =2)
#TRYING TO ADD CHECK BUTTONS
#pla_received_y=Checkbutton(root,text="YES",variable=vary)
#pla_received_y.grid(row=29,column =1)
#pla_received_n=Checkbutton(root,text="NO",variable=varn)
#pla_received_n.grid(row = 29 , column =2)
pla_company_name =Entry(root,width=50)
pla_company_name .grid(row=30,column =1)
#ACTIVITY COORDINATOR
acname=Entry(root,width=50)
acname.grid(row=1,column =5)
stu_name=Entry(root,width=50)
stu_name.grid(row=2,column =5)
iv_vis=Entry(root,width=50)
iv_vis.grid(row=3,column =5)
loc_for_iv=Entry(root,width=50)
loc_for_iv.grid(row=4,column =5)
mi1_project_name=Entry(root,width=50)
mi1_project_name.grid(row=5,column =5)
mi1_mentor=Entry(root,width=50)
mi1_mentor.grid(row=6,column =5)
mi2_project_name=Entry(root,width=50)
mi2_project_name.grid(row=7,column =5)
mi2_mentor=Entry(root,width=50)
mi2_mentor.grid(row=8,column =5)
ma1_project_name=Entry(root,width=50)
ma1_project_name.grid(row=9,column =5)
ma1_mentor=Entry(root,width=50)
ma1_mentor.grid(row=10,column =5)
ma2_project_name=Entry(root,width=50)
ma2_project_name.grid(row=11,column =5)
ma2_mentor=Entry(root,width=50)
ma2_mentor.grid(row=12,column =5)
#COURSE COORDINATOR
cc_name=Entry(root,width=50)
cc_name.grid(row=47,column =1)
name_of_student=Entry(root,width=50)
name_of_student.grid(row=48,column =1)
certification_done=Entry(root,width=50)
certification_done.grid(row=49,column =1)
achievements=Entry(root,width=50)
achievements.grid(row=50,column =1)

delete=Entry(root,width=25)
delete.grid(row=19,column=4)



#CREATE TEXT BOX LABELS

s_no_label=Label(root, text ="Serial Number",justify=RIGHT)
s_no_label.grid(row=1,column=0)
name_of_project_label=Label(root, text ="Name Of Project",justify=CENTER)
name_of_project_label.grid(row=2,column=0)
co_inv_label=Label(root, text ="Co-Investigator",justify=LEFT)
co_inv_label.grid(row=3,column=0)
name_of_funding_agency_label=Label(root, text ="Name Of Funding Agency",justify=RIGHT)
name_of_funding_agency_label.grid(row=4,column=0)
type_label=Label(root,text="Type (Government/ Non-Government)",justify=RIGHT)
type_label.grid(row=5,column=0)
dept_label=Label(root,text="Department of Principal Investigator/ Co Investigator",justify=RIGHT)
dept_label.grid(row=6, column=0)
year_label=Label(root,text="Year of Award",justify=RIGHT)
year_label.grid(row=7, column=0)
fund_label=Label(root,text="Funds provided (INR in lakhs) ",justify=RIGHT)
fund_label.grid(row=8, column=0)
dur_label=Label(root,text="Duration of the project",justify=RIGHT)
dur_label.grid(row=9, column=0)
link1_label=Label(root,text="Link of the Sanctioned Letter",justify=RIGHT)
link1_label.grid(row=10, column=0)
link2_label=Label(root,text="Link of the Utalization Certificate",justify=RIGHT)
link2_label.grid(row=11, column=0)
name_prog_label=Label(root,text="Name of Program",justify=RIGHT)
name_prog_label.grid(row=14, column=0)
type_prog_label=Label(root,text="Type of Program",justify=RIGHT)
type_prog_label.grid(row=15, column=0)
prog_code_label=Label(root,text="Program Code",justify=RIGHT)
prog_code_label.grid(row=16, column=0)
spe_label=Label(root,text="Specialisation",justify=RIGHT)
spe_label.grid(row=17, column=0)
rev_cour_label=Label(root,text="Revised Course",justify=RIGHT)
rev_cour_label.grid(row=18, column=0)
#PIC_DETAILS
name_of_pic_label=Label(root,text="Name of PIC",justify=RIGHT)
name_of_pic_label.grid(row=21, column=0)
name_of_stu_label =Label(root,text="Name of Student",justify=RIGHT)
name_of_stu_label .grid(row=22, column=0)
course_label=Label(root,text="Course",justify=RIGHT)
course_label.grid(row=23, column=0)
sap_id_label=Label(root,text="SAP ID",justify=RIGHT)
sap_id_label.grid(row=24, column=0)
roll_no_label=Label(root,text="ROLL NUMBER",justify=RIGHT)
roll_no_label.grid(row=25, column=0)
internship_done_label=Label(root,text="Internship Done",justify=RIGHT)
internship_done_label.grid(row=26, column=0)
internship_company_name_label=Label(root,text="Internship Company Name",justify=RIGHT)
internship_company_name_label.grid(row=27, column=0)
opt_for_placement_program_label=Label(root,text="Opted for Placement Program",justify=RIGHT)
opt_for_placement_program_label.grid(row=28, column=0)
placement_received_label=Label(root,text="Placement Received",justify=RIGHT)
placement_received_label.grid(row=29, column=0)
placed_company_name_label=Label(root,text="Placed Company Name",justify=RIGHT)
placed_company_name_label.grid(row=30, column=0)
#ACTIVITY_COORDINATOR
ac_name_label=Label(root,text="AC Name",justify=RIGHT)
ac_name_label.grid(row=1, column=4)
student_name_label=Label(root,text="Student Name",justify=RIGHT)
student_name_label.grid(row=2, column=4)
iv_visited_label=Label(root,text="IV visited",justify=RIGHT)
iv_visited_label.grid(row=3, column=4)
location_for_iv_label=Label(root,text="Location for IV",justify=RIGHT)
location_for_iv_label.grid(row=4, column=4)
minor1_project_name_label=Label(root,text="Minor 1 Project Name",justify=RIGHT)
minor1_project_name_label.grid(row=5, column=4)
minor1_mentor_label=Label(root,text="Minor 1 Mentor Name",justify=RIGHT)
minor1_mentor_label.grid(row=6, column=4)
minor2_project_name_label=Label(root,text="Minor 2 Project Name",justify=RIGHT)
minor2_project_name_label.grid(row=7, column=4)
minor2_mentor_label=Label(root,text="Minor 2 Mentor Name",justify=RIGHT)
minor2_mentor_label.grid(row=8, column=4)
major1_project_name_label=Label(root,text="Major 1 Project Name",justify=RIGHT)
major1_project_name_label.grid(row=9, column=4)
major2_mentor_label=Label(root,text="Major 1 Mentor Name",justify=RIGHT)
major2_mentor_label.grid(row=10, column=4)
major2_project_name_label=Label(root,text="Major 2 Project Name",justify=RIGHT)
major2_project_name_label.grid(row=11, column=4)
major2_mentor_label =Label(root,text="Major 2 Mentor Name",justify=RIGHT)
major2_mentor_label .grid(row=12, column=4)

#COURSE_COORDINATOR
cc_name_label=Label(root,text="CC Name",justify=RIGHT)
cc_name_label.grid(row=47, column=0)
name_of_student_label =Label(root,text="Name of Student",justify=RIGHT)
name_of_student_label .grid(row=48, column=0)
certification_done_label=Label(root,text="Certification Done",justify=RIGHT)
certification_done_label.grid(row=49, column=0)
achievements_label=Label(root,text="Achievements",justify=RIGHT)
achievements_label.grid(row=50, column=0)

#DELETE BUTTON
delete_label=Label(root,text="DELETE ID ",justify=CENTER)
delete_label.grid(row=19,column=3)





#CREATE SUBMIT BUTTON

submit_btn=Button(root, text="Add Record to Database", command = submit)
submit_btn.grid(row=15, column = 4, columnspan=2,ipadx=75)


#CREATE A QUERY BUTTON
query_btn = Button(root,text= "Show Records",command=query)
query_btn.grid(row = 17 ,column = 4 , columnspan=2,ipadx=75)

#CREATE A DELETE BUTTON
query_btn = Button(root,text= "Delete Record",command=delete)
query_btn.grid(row = 19 ,column = 5 , columnspan=2,ipadx=75)

#COMMIT CONNECTION
conn.commit()
# close connection
conn.close()

root.mainloop()