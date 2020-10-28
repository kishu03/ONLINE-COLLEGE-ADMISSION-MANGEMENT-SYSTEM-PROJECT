from tkinter import *
class Admission:
    def __init__(self,root):
        self.root=root
        self.root.title("College Admission Management System")
        self.root.geometry("1000x520")
        self.root.resizable(0,0)


        f2 = Frame(self.root, borderwidth=8, bg="grey", relief=SUNKEN)
        f2.pack(side=TOP, fill="x")
        title = Label(f2,text="College Admission Management System", font=("bold", 20), fg="green", bd=5, relief=SUNKEN, bg="black")
        title.pack(side="top")
        f1 = Frame(self.root, bg="grey", borderwidth=6, relief=SUNKEN)
        f1.place(x=7,y=65,height=450,width=450)
        a=Label(f1, text="Enter Student Details", font=10, bg="green", bd=7)
        a.grid(columnspan=3,pady=10)
        name = Label(f1, text="Name", font=5, bg="yellow", bd=4)
        name.grid(row=1,pady=10,padx=5)
        namee=Entry(f1, font=8, bd=6)
        namee.grid(row=1,column=2,padx=60)
        Branch = Label(f1, text="Branch Name", font=(5), bg="yellow", bd=4)
        Branch.grid(row=2, pady=10, padx=5)
        branchh= Entry(f1, font=(8), bd=6)
        branchh.grid(row=2, column=2, padx=60)
        dob = Label(f1, text="Date-Of-Birth", font=(5), bg="yellow", bd=4)
        dob.grid(row=3, pady=10, padx=5)
        DOB= Entry(f1, font=(8), bd=6)
        DOB.grid(row=3, column=2)
        reg= Label(f1, text="Registration No", font=(5), bg="yellow", bd=4)
        reg.grid(row=4, pady=10, padx=5)
        REG = Entry(f1, font=(8), bd=6)
        REG.grid(row=4, column=2)
        sec = Label(f1, text="Section", font=(5), bg="yellow", bd=4)
        sec.grid(row=6, pady=10, padx=5)
        SEC = Entry(f1, font=(8), bd=6)
        SEC.grid(row=6, column=2)
        gen= Label(f1, text="Gender", font=(5), bg="yellow", bd=4)
        gen.grid(row=5, pady=10, padx=5)
        values=["male","female","others"]
        variable=StringVar(f1)
        variable.set("Select")
        drop=OptionMenu(f1,variable,*values)
        drop.grid(row=5, column=2)

        frame3= Frame(self.root, bg="grey", borderwidth=6, relief=SUNKEN)
        frame3.place(x=7, y=460, width=450)
        button1=Button(frame3,text="Add",width=10).grid(row=0,column=0,padx=10,pady=10)
        button2 = Button(frame3, text="Update", width=10).grid(row=0, column=1, padx=10, pady=10)
        button3 = Button(frame3, text="Delete", width=10).grid(row=0, column=2, padx=10, pady=10)
        button4 = Button(frame3, text="Clear", width=10).grid(row=0, column=3, padx=10, pady=10)


        frame4= Frame(self.root, bg="grey", borderwidth=6, relief=SUNKEN)
        frame4.place(x=465, y=65, width=530,height=450)

        search=Label(frame4,text="Search By",font=(5), bg="green", bd=6)
        search.grid(padx=10,pady=10)
        values = ["Name", "Reg no", "Section"]
        variable = StringVar(frame4)
        variable.set("Select")
        drop = OptionMenu(frame4, variable, *values)
        drop.grid(column=1,row=0)
        s = Entry(frame4, font=(4), bd=6)
        s.grid(row=0, column=2,padx=15)

        butto = Button(frame4, text="Search", width=10).grid(row=0, column=3, padx=14, pady=6)

        frame5 = Frame(frame4, bg="grey", borderwidth=6, relief=SUNKEN)
        frame5.place(x=5, y=60, width=500, height=380)
root= Tk()
object=Admission(root)
root.mainloop()


