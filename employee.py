from tkinter import*
from tkinter import  ttk
from PIL import Image,ImageTk
import mysql.connector
from tkinter import messagebox

class Employee:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("Employee Management System")
       
        #variables
        self.var_dep=StringVar()
        self.var_name=StringVar()
        self.var_designition=StringVar()
        self.var_email=StringVar()
        self.var_address=StringVar()
        self.var_married=StringVar()
        self.var_dob=StringVar()
        self.var_doj=StringVar()
        self.var_idproofcomb=StringVar()
        self.var_idproof=StringVar()
        self.var_gender=StringVar()
        self.var_phone=StringVar()
        self.var_country=StringVar()
        self.var_salary=StringVar()

        leb_title=Label(self.root,text="EMPLOYEE MANAGEMENT SYSTEM",font=("times new roman",37,'bold'),fg='darkred',bg='black')
        leb_title.place(x=0,y=0,width=1530,height=50)
        
        # logo 
        img_logo=Image.open('images/10.jpeg')#This specifies the desired width and height of the resized image. 
                                            #In this case, the image is being resized to a width of 50 pixels and a height of 50 pixels.
        image_logo=img_logo.resize((50,50),Image.ANTIALIAS)#ANTIALIAS convert the quality of image highe to lowlevel image  
        self.photo_logo=ImageTk.PhotoImage(image_logo)
        self.logo=Label(self.root,image=self.photo_logo)
        self.logo.place(x=270,y=0,width=50,height=50)
       
        #working on frame 
        img_frame=Frame(self.root,bd=5,relief=RIDGE,bg="yellow")
        img_frame.place(x=0,y=50,width=1530,height=160)

        # 1st _2
        img2=Image.open('images/9.jpeg')
        img2=img2.resize((518,160),Image.ANTIALIAS)#ANTIALIAS convert the quality of image highe to lowlevel image  
        self.photo1=ImageTk.PhotoImage(img2)
        self.img_1=Label(img_frame,image=self.photo1)
        self.img_1.place(x=0,y=0,width=490,height=160)
        
        img_2=Image.open('images/1.jpeg')    
        img_2=img_2.resize((518,160),Image.ANTIALIAS)#ANTIALIAS convert the quality of image highe to lowlevel image  
        self.photo2=ImageTk.PhotoImage(img_2)
        self.img_2=Label(img_frame,image=self.photo2)
        self.img_2.place(x=490,y=0,width=518,height=160)


        #3rd image
        imag_3=Image.open('images/3.jpeg')
        imag_3=imag_3.resize((518,160),Image.ANTIALIAS)#ANTIALIAS convert the quality of image highe to lowlevel image  
        self.photo3=ImageTk.PhotoImage(imag_3)
        self.img_3=Label(img_frame,image=self.photo3)
        self.img_3.place(x=1000,y=0,width=518,height=160)

        #main frame 
        Main_frame=Frame(self.root,bd=2,relief=RIDGE,bg="dark green")
        Main_frame.place(x=10,y=220,width=1500,height=560)

        # upper frame #################### IN LABLE FRAME WE CAN GIVE TEXT 
        Upper_frame=LabelFrame(Main_frame,bd=2,relief=RIDGE,bg="dark gray",text="Employee Information ",font=("times new roman",11,'bold'),fg='dark red')
        Upper_frame.place(x=10,y=10,width=1480,height=270)

        # Lables and entry fields
        lbl_dep=Label(Upper_frame,text="Department",font=("arial",11,'bold'),bg='white')
        lbl_dep.grid(row=0,column=0,padx=2,sticky=W)

        combo_dep=ttk.Combobox(Upper_frame,textvariable=self.var_dep,font=("times new roman",12,'bold'),width=21,state='readonly')
        combo_dep['value']=('Select Department','Human Resources (HR)','Information Technology (IT)','Marketing',"Finance","Customer Support","Research and Development (R&D)")
        combo_dep.current(0)
        combo_dep.grid(row=0,column=1,padx=2,pady=10,sticky=W)
        
        #name
        lbl_Name=Label(Upper_frame,font=("arial",12,'bold'),text='Name:',bg='white')
        lbl_Name.grid(row=0,column=2,sticky=W,padx=2,pady=7)

        text_name=ttk.Entry(Upper_frame,textvariable=self.var_name,width=22,font=("arial",11,"bold"))
        text_name.grid(row=0,column=3,padx=2,pady=7)

        # labl_DesigniDesignition
        lbl_Designition=Label(Upper_frame,font=("arial",12,'bold'),text='Designition:',bg='white')
        lbl_Designition.grid(row=1,column=0,sticky=W,padx=2,pady=7)

        text_Designition=ttk.Entry(Upper_frame,textvariable=self.var_designition,width=22,font=("arial",11,"bold"))
        text_Designition.grid(row=1,column=1,padx=2,pady=7,sticky=W)
           #E-mail
        lbl_email=Label(Upper_frame,font=("arial",12,'bold'),text='Email:',bg='white')
        lbl_email.grid(row=1,column=2,sticky=W,padx=2,pady=7)

        text_email=ttk.Entry(Upper_frame,textvariable=self.var_email,width=22,font=("arial",11,"bold"))
        text_email.grid(row=1,column=3,padx=2,pady=7)

        #address
        lbl_address=Label(Upper_frame,font=("arial",12,'bold'),text='Address:',bg='white')
        lbl_address.grid(row=2,column=0,sticky=W,padx=2,pady=7)

        text_address=ttk.Entry(Upper_frame,textvariable=self.var_address,width=22,font=("arial",11,"bold"))
        text_address.grid(row=2,column=1,padx=2,pady=7,sticky=W)

        #married
        lbl_merried=Label(Upper_frame,font=("arial",12,'bold'),text='Married status:',bg='white')
        lbl_merried.grid(row=2,column=2,sticky=W,padx=2,pady=7)


        com_txt_married=ttk.Combobox(Upper_frame,textvariable=self.var_married,state="readonly",font=("arial",12,"bold"),width=18)
        com_txt_married['value']=("Select","Married","Unmarried")
        com_txt_married.current(0)
        com_txt_married.grid(row=2,column=3,sticky=W,padx=2,pady=7)

        #dob
        lbl_dob=Label(Upper_frame,font=("arial",12,'bold'),text='DOB:',bg='white')
        lbl_dob.grid(row=3,column=0,sticky=W,padx=2,pady=7)

        text_dob=ttk.Entry(Upper_frame,textvariable=self.var_dob,width=22,font=("arial",11,"bold"))
        text_dob.grid(row=3,column=1,padx=2,pady=7)

        #doj
        lbl_Doj=Label(Upper_frame,font=("arial",12,'bold'),text='DOj:',bg='white')
        lbl_Doj.grid(row=3,column=2,sticky=W,padx=2,pady=7)

        text_Doj=ttk.Entry(Upper_frame,textvariable=self.var_doj,width=22,font=("arial",11,"bold"))
        text_Doj.grid(row=3,column=3,padx=2,pady=7)

        #ID 
        
        com_txt_proof=ttk.Combobox(Upper_frame,textvariable=self.var_idproofcomb,state="readonly",font=("arial",12,"bold"),width=18)
        com_txt_proof['value']=("select ID proof","PAN CARD", "ADHAR CARD" ,"DRIVING LICENCE","VOTER ID","PASSPORT ID")
        com_txt_proof.current(0)
        com_txt_proof.grid(row=4,column=0,sticky=W,padx=2,pady=7)

        text_proof=ttk.Entry(Upper_frame,textvariable=self.var_idproof,width=22,font=("arial",11,"bold"))
        text_proof.grid(row=4,column=1,padx=2,pady=7)

        #gender
        lbl_gender=Label(Upper_frame,font=("arial",12,'bold'),text='Gender:',bg='white')
        lbl_gender.grid(row=4,column=2,sticky=W,padx=2,pady=7)

        com_txt_gender=ttk.Combobox(Upper_frame,textvariable=self.var_gender,state="readonly",font=("arial",12,"bold"),width=18)
        com_txt_gender['value']=("select ","Male", "female", "Other")
        com_txt_gender.current(0)
        com_txt_gender.grid(row=4,column=3,sticky=W,padx=2,pady=7)

        #phone
        lbl_phone=Label(Upper_frame,font=("arial",12,'bold'),text='Phone No:',bg='white')
        lbl_phone.grid(row=0,column=4,sticky=W,padx=2,pady=7)

        txt_phone=ttk.Entry(Upper_frame,textvariable=self.var_phone,width=22,font=("arial",11,"bold"))
        txt_phone.grid(row=0,column=5,padx=2,pady=7)

        #country
        lbl_country=Label(Upper_frame,font=("arial",12,'bold'),text='Country:',bg='white')
        lbl_country.grid(row=1,column=4,sticky=W,padx=2,pady=7)

        txt_country=ttk.Entry(Upper_frame,textvariable=self.var_country,width=22,font=("arial",11,"bold"))
        txt_country.grid(row=1,column=5,padx=2,pady=7)

        #ctc
        lbl_ctc=Label(Upper_frame,font=("arial",12,'bold'),text='Salary(CTC):',bg='white')
        lbl_ctc.grid(row=2,column=4,sticky=W,padx=2,pady=7)

        txt_ctc=ttk.Entry(Upper_frame,textvariable=self.var_salary,width=22,font=("arial",11,"bold"))
        txt_ctc.grid(row=2,column=5,padx=2,pady=7)

        #mask image
        img_mask=Image.open('images/6.jpeg')
        img_mask=img_mask.resize((220,220),Image.ANTIALIAS)#ANTIALIAS convert the quality of image highe to lowlevel image  
        self.photomask=ImageTk.PhotoImage(img_mask)
        self.img_mask=Label(Upper_frame,image=self.photomask)
        self.img_mask.place(x=1000,y=0,width=220,height=220)


        #button frame 
        button_frame=Frame(Upper_frame,bd=2,relief=RIDGE,bg="white")
        button_frame.place(x=1290,y=20,width=170,height=210)

        btn_add=Button(button_frame,text='Save',command=self.add_data,font=("arial",15,'bold'),width=13,bg='green',fg='white')
        btn_add.grid(row=0,column=0,padx=1,pady=5)


        btn_update=Button(button_frame,text='Update',command=self.update_data,font=("arial",15,'bold'),width=13,bg='blue',fg='white')
        btn_update.grid(row=1,column=0,padx=1,pady=5)


        btn_delete=Button(button_frame,text='Delete',command=self.delete_data,font=("arial",15,'bold'),width=13,bg='dark red',fg='white')
        btn_delete.grid(row=2,column=0,padx=1,pady=5)


        btn_clear=Button(button_frame,text='Clear',command=self.reset_data,font=("arial",15,'bold'),width=13,bg='magenta',fg='white')
        btn_clear.grid(row=3,column=0,padx=1,pady=5)

        #down frame 
        Down_frame=LabelFrame(Main_frame,bd=2,relief=RIDGE,bg="dark blue",text="Employee Information",font=("times new roman",11,'bold'),fg='red')
        Down_frame.place(x=10,y=280,width=1480,height=270)
        
        #search frame
        search_frame=LabelFrame(Down_frame,bd=2,relief=RIDGE,bg="yellow",text="Search Employee information",font=("times new roman",11,'bold'),fg='dark red')
        search_frame.place(x=0,y=0,width=1470,height=60)
        
        search_by=Label(search_frame,font=("arial",11,"bold"),text="search by:",fg="white",bg="dark red")
        search_by.grid(row=0,column=0,sticky=W,padx=5)

        #search
        
        self.var_com_search=StringVar()
        com_txt_search=ttk.Combobox(search_frame,textvariable=self.var_com_search,state="readonly",
                             font=("arial",12,"bold"),width=18)
        com_txt_search['value']=("sealect option","phone","id_proof","email")
        com_txt_search.current(0)
        com_txt_search.grid(row=0,column=1,sticky=W,padx=5)

        self.var_search=StringVar()
        txt_search=ttk.Entry(search_frame,textvariable=self.var_search,width=22,font=("arial",11,"bold"))
        txt_search.grid(row=0,column=2,padx=5)

        btn_search=Button(search_frame,text="search",command=self.search_data,font=("arial",11,"bold"),width=14,fg="white",bg="blue")
        btn_search.grid(row=0,column=3,padx=5)

        btn_showall=Button(search_frame,text="show all",command=self.fetch_data,font=("arial",11,"bold"),width=14,fg="white",bg="blue")
        btn_showall.grid(row=0,column=4,padx=5)

        stayhome=Label(search_frame,text="WEAR A MASK",font=("times new roman",30,"bold"),fg="red",bg="yellow")
        stayhome.place(x=760,y=0,width=600,height=30)


       

        img_logo_mask=Image.open('images/11.jpeg')
        img_logo_mask=img_logo_mask.resize((50,50),Image.ANTIALIAS)#ANTIALIAS convert the quality of image highe to lowlevel image  
        self.photoimg_logo_mask=ImageTk.PhotoImage(img_logo_mask)
        self.logo=Label(search_frame,image=self.photoimg_logo_mask)
        self.logo.place(x=860,y=0,width=50,height=30)






        imgz=Image.open('images/11.jpeg')
        imgz=imgz.resize((50,50),Image.ANTIALIAS)#ANTIALIAS convert the quality of image highe to lowlevel image  
        self.photoimgy=ImageTk.PhotoImage(imgz)
        self.logo=Label(search_frame,image=self.photoimgy)
        self.logo.place(x=1240,y=0,width=50,height=30)




        ######## Employee table**************************************************
        table_frame=Frame(Down_frame,bd=3,relief=RIDGE)
        table_frame.place(x=0,y=60,width=1470,height=170)

        scroll_x=ttk.Scrollbar(table_frame,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(table_frame,orient=VERTICAL)
                                                                    #below are the dummy name only
        self.employee_table=ttk.Treeview(table_frame,column=('dep','name','degi','email','address','married','dob','doj','idproofcomb','idproof'
                                                             ,'gender','phone','country','salary',),xscrollcommand=scroll_x.set,
                                                             yscrollcommand=scroll_y.set) # tk.Treeview widget allows you
                                                                                          ####to display and manipulate hierarchical data in a tree-like structure.
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)

        scroll_x.config(command=self.employee_table.xview)
        scroll_y.config(command=self.employee_table.yview)
        
        self.employee_table.heading('dep', text='Department')
        self.employee_table.heading('name', text='Name')
        self.employee_table.heading('degi', text='Deginition')
        self.employee_table.heading('email', text='Email')
        self.employee_table.heading('address', text='Address')
        self.employee_table.heading('married', text='Married Status')
        self.employee_table.heading('dob', text='DOB')
        self.employee_table.heading('doj', text='DOJ')
        self.employee_table.heading('idproofcomb', text='ID Type')
        self.employee_table.heading('idproof', text='ID proof')
        self.employee_table.heading('gender', text='gender')
        self.employee_table.heading('phone', text='Phone')
        self.employee_table.heading('country', text='Country')
        self.employee_table.heading('salary', text='Salary')
        
        self.employee_table['show']='headings'
        self.employee_table.column("dep",width=200)
        self.employee_table.column("name",width=140)
        self.employee_table.column("degi",width=170)
        self.employee_table.column("email",width=150)
        self.employee_table.column("address",width=100)
        self.employee_table.column("married",width=100)
        self.employee_table.column("dob",width=100)
        self.employee_table.column("doj",width=100)
        self.employee_table.column("idproofcomb",width=150)
        self.employee_table.column("idproof",width=100)
        self.employee_table.column("gender",width=70)
        self.employee_table.column("phone",width=100)
        self.employee_table.column("country",width=80)
        self.employee_table.column("salary",width=80)
        


        self.employee_table.pack(fill=BOTH,expand=1) #fill=BOTH option ensures that the widget expands both horizontally and vertically 
        #                                             to fill the available space.
        self.employee_table.bind("<ButtonRelease>",self.get_cursor)# method for bind to get data on screen 


#When expand=1 is set for a widget, it means that the widget is allowed to expand and occupy any 
# additional space in the parent container that is not taken up by other widgets. The widget will maintain its proportions relative to other widgets. 
# If you set expand=2 in the pack() method, it means that the widget will 
# try to expand and occupy twice the amount of extra space compared to other widgets in the same container.
        self.fetch_data()


    #************function declarations*************************8
    def add_data(self):
      if self.var_dep.get()=="" or self.var_email.get()=="" or self.var_email.get()=="" or self.var_designition.get()=="" or self.var_salary.get()=="" or self.var_com_search.get()=="" or self.var_dob.get()=="" or self.var_doj.get()=="" or self.var_address.get()=="" or self.var_name.get()=="" or self.var_phone.get()=="" or self.var_idproof.get()=="" or self.var_idproofcomb.get()=="select ID proof" or self.var_married.get()=="Select"or self.var_gender.get()=="select ":
        messagebox.showerror('Error','ALL Fields are required')
      else:
        try:
            conn = mysql.connector.connect(host="localhost", user="root", password="Adarsh13@#$", database="sys")
            my_cursor = conn.cursor()#In database programming, the cursor() #method is typically used to create a cursor object associated with a database connection.
            #The cursor object allows you to execute SQL queries, fetch data, and perform other operations on the database.



            # cursor as an object or pointer that helps you navigate and access data in a result set, while the execute() method is responsible for executing SQL statements against the database.
            




            my_cursor.execute('INSERT INTO employee  values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)',#hear %S is space holder for sql query
                (self.var_dep.get(),
                 self.var_name.get(),
                 self.var_designition.get(),
                 self.var_email.get(),
                 self.var_address.get(),
                 self.var_married.get(),
                 self.var_dob.get(),
                 self.var_doj.get(),
                 self.var_idproofcomb.get(),
                 self.var_idproof.get(),
                 self.var_gender.get(),
                 self.var_phone.get(),
                 self.var_country.get(),
                 self.var_salary.get()
                ))
            conn.commit() # The conn.commit() method is used to save the changes made to a database after a transaction has been successfully completed.
            self.fetch_data()
            conn.close()
            messagebox.showinfo('Success','Employee has been added!',parent=self.root)
        except Exception as es:
            messagebox.showerror('Error',f'Due To:{str(es)}',parent=self.root)
                #function is called in it button 


    #fatch data
    def fetch_data(self):
       conn = mysql.connector.connect(host="localhost", user="root", password="Adarsh13@#$", database="sys")
       my_cursor = conn.cursor()
       my_cursor.execute('select * from employee')
       data=my_cursor.fetchall()
       if len(data)!=0:
            self.employee_table.delete(*self.employee_table.get_children())#get children is method it represent the attribute like dipartment name and so on)
            for i in data:
               self.employee_table.insert("",END,values=i)
            conn.commit()
            conn.close()
    

    #get cursor to get data on screen
    def get_cursor(self,event=''):
       cursor_row=self.employee_table.focus() #it is a method to focus table 
       content=self.employee_table.item(cursor_row)# whatever item in that cursor row that we take 
       data=content['values']


       self.var_dep.set(data[0])
       self.var_name.set(data[1])
       self.var_designition.set(data[2])
       self.var_email.set(data[3])
       self.var_address.set(data[4])
       self.var_married.set(data[5])
       self.var_dob.set(data[6])
       self.var_doj.set(data[7])
       self.var_idproofcomb.set(data[8])
       self.var_idproof.set(data[9])
       self.var_gender.set(data[10])
       self.var_phone.set(data[11])
       self.var_country.set(data[12])
       self.var_salary.set(data[13])
    
    #update
    def update_data(self):
      if self.var_dep.get()=="" or self.var_email.get()=="" or self.var_designition.get()=="" or self.var_salary.get()=="" or self.var_com_search.get()=="" or self.var_dob.get()=="" or self.var_doj.get()=="" or self.var_address.get()=="" or self.var_name.get()=="" or self.var_phone.get()=="" or self.var_idproof.get()=="" or self.var_idproofcomb.get()=="select ID proof" or self.var_married.get()=="Select"or self.var_gender.get()=="select ":
        messagebox.showerror('Error','ALL Fields are required')
      else:
        try:
            update=messagebox.askyesno('Update','Are you sure about update the profile of Employee data')
            if update>0:
                conn = mysql.connector.connect(host="localhost", user="root", password="Adarsh13@#$", database="sys")
                my_cursor = conn.cursor()
                my_cursor.execute('update employee set Department=%s,Name=%s,Designition=%s,Email=%s,Address=%s,Married_status=%s,DOB=%s,DOJ=%s,id_proof_type=%s,Gender=%s,Phone=%s,Country=%s,Salary=%s where id_proof=%s',(
                                  

                 self.var_dep.get(),
                 self.var_name.get(),
                 self.var_designition.get(),
                 self.var_email.get(),
                 self.var_address.get(),
                 self.var_married.get(),
                 self.var_dob.get(),
                 self.var_doj.get(),
                 self.var_idproofcomb.get(),
                 
                 self.var_gender.get(),
                 self.var_phone.get(),
                 self.var_country.get(),
                 self.var_salary.get(),
                 self.var_idproof.get()                                                                                                                                                                                         
                                                                                              ))
            else:
               if not update:
                  return
            conn.commit()
            self.fetch_data()
            conn.close()
            messagebox.showinfo('success','Employee successfuully updated',parent=self.root)
        except Exception as es:
            messagebox.showerror('Error',f'Due To:{str(es)}',parent=self.root)

    #delete
    def delete_data(self):
      if self.var_idproof.get() == "":
        messagebox.showerror('Error', 'All fields are required')
      else:
        try:
            Delete = messagebox.askyesno('Delete', 'Are you sure to delete this Employee', parent=self.root)
            if Delete > 0:
                conn = mysql.connector.connect(host="localhost", user="root", password="Adarsh13@#$", database="sys")
                my_cursor = conn.cursor()
                sql = 'delete from employee where id_proof=%s'
                value = (self.var_idproof.get(),)
                my_cursor.execute(sql,value)
                    
               
            else:
                if not Delete:
                    return
            conn.commit()
            self.fetch_data()
            conn.close()
            messagebox.showinfo('Deleted','Employee successfuully Deleted',parent=self.root)
        except Exception as es:
            messagebox.showerror('Error',f'Due To:{str(es)}',parent=self.root)

              
    #reset
    def reset_data(self):
       
       self.var_dep.set("Select Department")
       self.var_name.set("")
       self.var_designition.set("")
       self.var_email.set("")
       self.var_address.set("")
       self.var_married.set("Select")
       self.var_dob.set("")
       self.var_doj.set("")
       self.var_idproofcomb.set("select ID proof")
       self.var_idproof.set("")
       self.var_gender.set("select ")
       self.var_phone.set("")
       self.var_country.set("")
       self.var_salary.set("")

    #search 
    def search_data(self):
        if self.var_com_search.get()=="" or self.var_search.get()=='':
          messagebox.showerror('Error','Please select option')
        else:
            try:
                conn = mysql.connector.connect(host="localhost", user="root", password="Adarsh13@#$", database="sys")
                my_cursor = conn.cursor()
                my_cursor.execute('select * from employee where ' +str(self.var_com_search.get())+" LIKE '%"+str(self.var_search.get()+"%'"))
                rows=my_cursor.fetchall()# it is dbms method 
                if len(rows)!=0:
                   self.employee_table.delete(*self.employee_table.get_children())
                   for i in rows:
                      self.employee_table.insert("",END,values=i)
                conn.commit()
                conn.close()
            except Exception as es:
                messagebox.showerror('Error',f'Due To:{str(es)}',parent=self.root)
    





    








root=Tk()
root.iconbitmap('a.ico')
obj=Employee(root)
root.mainloop()
