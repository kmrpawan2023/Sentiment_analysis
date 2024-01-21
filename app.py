import tkinter
from tkinter import *
from tkinter import messagebox
from mydb import Database
class NlpApp:
    def __init__(self):
        self.dbo = Database()
        self.root = Tk()
        self.root.title('NlpApp')
       # self.root.iconbitmap('nlpapp/resources/fevicon.ico.ico')
       # self.root.geometry('350 x 600')
        self.root.configure(bg="#839192")
        self.login_gui()
        self.root.mainloop()

    def login_gui(self):
        self.clear()
        heading = Label(self.root,text='NlpApp',bg="#839192",fg='white')
        heading.pack(pady=(30,30))
        heading.configure(font=('verdana',24,'bold'))
        
        label1 = Label(self.root,text = 'email id')
        label1.pack(pady =(10,10))
        self.enter_email = Entry(self.root,width=30)
        self.enter_email.pack(pady = (5,10),ipady=4)

        label2 = Label(self.root,text = 'password')
        label2.pack(pady =(10,10))
        self.enter_password = Entry(self.root,width=30,show='*')
        self.enter_password.pack(pady = (5,10),ipady=4)

        login_btn = Button(self.root,text = 'login',width=30,height=2)
        login_btn.pack(pady = (10,10))
        
        label3 = Label(self.root,text = 'Not a member?',width = 20 ,height =2)
        label3.pack(pady =(20,10))
        redirect_btn = Button(self.root,text = 'register',width=15,height=1,command=self.register_gui)
        redirect_btn.pack(pady = (10,10))
        
    def register_gui(self):
        #clear the existing gui
        self.clear()
        heading = Label(self.root,text='NlpApp',bg="#839192",fg='white')
        heading.pack(pady=(30,30))
        heading.configure(font=('verdana',24,'bold'))

        label0 = Label(self.root,text = 'enter name')
        label0.pack(pady =(10,10))
        self.enter_name = Entry(self.root,width=30)
        self.enter_name.pack(pady = (5,10),ipady=4)
        
        label1 = Label(self.root,text = 'email id')
        label1.pack(pady =(10,10))
        self.enter_email = Entry(self.root,width=30)
        self.enter_email.pack(pady = (5,10),ipady=4)

        label2 = Label(self.root,text = 'password')
        label2.pack(pady =(10,10))
        self.enter_password = Entry(self.root,width=30,show='*')
        self.enter_password.pack(pady = (5,10),ipady=4)

        register_btn = Button(self.root,text = 'register',width=30,height=2,command= self.perform_registration)
        register_btn.pack(pady = (10,10))
        
        label3 = Label(self.root,text = 'already a member?',width = 20 ,height =2)
        label3.pack(pady =(20,10))
        redirect_btn = Button(self.root,text = 'login now',width=15,height=1,command=self.login_gui)
        redirect_btn.pack(pady = (10,10))
        

    def clear(self):
        
        for i in self.root.pack_slaves():
            i.destroy()

    def perform_registration(self):
        #fetch data from gui
        name = self.enter_name.get() 
          
        email = self.enter_email.get()        
        password = self.enter_password.get() 

        response=self.dbo.add_data(name,email,password)  
        
        if response:
            messagebox.showinfo("success","registration complete you can now login")

        else:
            messagebox.showerror('error','email exist')   


nlp = NlpApp()        
