from tkinter import*
from tkinter import ttk
import tkinter
from turtle import bgcolor
from PIL import Image,ImageTk
import os
from time import strftime
from datetime import datetime
import time
# import pyttsx3
from student import Student
from train import Train
from face_recognition import Face_Recognition
from attendance import Attendance
from developer import Developer
from helpsupport import Helpsupport



class Face_Recognition_System:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition System")
        self.root.wm_iconbitmap("face.ico")

        # first image
        img=Image.open(r"images\27.jpg")
        img=img.resize((255,130),Image.ANTIALIAS)
        self.photoimg=ImageTk.PhotoImage(img)

        f_lbl=Label(self.root,image=self.photoimg)
        f_lbl.place(x=0,y=0,width=255,height=130)

        # second image
        img1=Image.open(r"images\34.jpg")
        img1=img1.resize((255,130),Image.ANTIALIAS)
        self.photoimg1=ImageTk.PhotoImage(img1)

        f_lbl=Label(self.root,image=self.photoimg1)
        f_lbl.place(x=255,y=0,width=255,height=130)

        # third image
        img2=Image.open(r"images\11.jpg")
        img2=img2.resize((255,130),Image.ANTIALIAS)
        self.photoimg2=ImageTk.PhotoImage(img2)

        f_lbl=Label(self.root,image=self.photoimg2)
        f_lbl.place(x=510,y=0,width=255,height=130)

        # fourth image
        img4=Image.open(r"images\17.jpg")
        img4=img4.resize((255,130),Image.ANTIALIAS)
        self.photoimg4=ImageTk.PhotoImage(img4)

        f_lbl=Label(self.root,image=self.photoimg4)
        f_lbl.place(x=765,y=0,width=255,height=130)

        # fifth image
        img5=Image.open(r"images\29.jpg")
        img5=img5.resize((255,130),Image.ANTIALIAS)
        self.photoimg5=ImageTk.PhotoImage(img5)

        f_lbl=Label(self.root,image=self.photoimg5)
        f_lbl.place(x=1020,y=0,width=255,height=130)

        # sixth image
        img6=Image.open(r"images\28.jpg")
        img6=img6.resize((255,130),Image.ANTIALIAS)
        self.photoimg6=ImageTk.PhotoImage(img6)

        f_lbl=Label(self.root,image=self.photoimg6)
        f_lbl.place(x=1275,y=0,width=255,height=130)

        # Bg image
        img_bg=Image.open(r"images\69.gif")
        img_bg=img_bg.resize((1530,660),Image.ANTIALIAS)
        self.photoimg_bg=ImageTk.PhotoImage(img_bg)

        f_lbl_img=Label(self.root,image=self.photoimg_bg)
        f_lbl_img.place(x=0,y=130,width=1530,height=660)

        title_lbl=Label(f_lbl_img,text="FACE RECOGNITION ATTENDANCE SYSTEM SOFTWARE",font=("times new roman",35,"bold"),bg="#1b1717",fg="#989898")
        title_lbl.place(x=0,y=0,width=1530,height=45)


        #########    Time   #############
        def time():
            cur_time = strftime('%H:%M:%S %p')
            lbl.config(text = cur_time)
            lbl.after(1000, time) 

        lbl = Label(title_lbl, font=("times new roman",14,"bold"),bg="#1b1717",fg="red") 
        lbl.place(x=0,y=0,width=110,height=50)   
        time()


        # student button
        img7=Image.open(r"images\37.jpg")
        img7=img7.resize((255,220),Image.ANTIALIAS)
        self.photoimg7=ImageTk.PhotoImage(img7)

        b1=Button(f_lbl_img,image=self.photoimg7,command=self.student_details,cursor="hand2")
        b1.place(x=200,y=100,width=220,height=220)

        b1_1=Button(f_lbl_img,text="Student Details",command=self.student_details,cursor="hand2",font=("times new roman",15,"bold"),bg="#000000",fg="white")
        b1_1.place(x=200,y=300,width=220,height=40)



        # Detect Face
        img8=Image.open(r"images\9.jpg")
        img8=img8.resize((255,220),Image.ANTIALIAS)
        self.photoimg8=ImageTk.PhotoImage(img8)

        b1=Button(f_lbl_img,image=self.photoimg8,cursor="hand2",command=self.face_data)
        b1.place(x=500,y=100,width=220,height=220)

        b1_1=Button(f_lbl_img,text="Face Detector",cursor="hand2",command=self.face_data,font=("times new roman",15,"bold"),bg="#000000",fg="white")
        b1_1.place(x=500,y=300,width=220,height=40)



        # Attendance
        img9=Image.open(r"images\35.jpg")
        img9=img9.resize((255,220),Image.ANTIALIAS)
        self.photoimg9=ImageTk.PhotoImage(img9)

        b1=Button(f_lbl_img,image=self.photoimg9,cursor="hand2",command=self.attendance_data)
        b1.place(x=800,y=100,width=220,height=220)

        b1_1=Button(f_lbl_img,text="Attendance",cursor="hand2",command=self.attendance_data,font=("times new roman",15,"bold"),bg="#000000",fg="white")
        b1_1.place(x=800,y=300,width=220,height=40)

        # Help
        img10=Image.open(r"images\47.jpg")
        img10=img10.resize((255,220),Image.ANTIALIAS)
        self.photoimg10=ImageTk.PhotoImage(img10)

        b1=Button(f_lbl_img,image=self.photoimg10,cursor="hand2",command=self.help_data)
        b1.place(x=1100,y=100,width=220,height=220)

        b1_1=Button(f_lbl_img,text="Help Desk",cursor="hand2",command=self.help_data,font=("times new roman",15,"bold"),bg="#000000",fg="white")
        b1_1.place(x=1100,y=300,width=220,height=40)

         # Train Face
        img11=Image.open(r"images\19.jpg")
        img11=img11.resize((255,220),Image.ANTIALIAS)
        self.photoimg11=ImageTk.PhotoImage(img11)

        b1=Button(f_lbl_img,image=self.photoimg11,cursor="hand2",command=self.train_data)
        b1.place(x=200,y=400,width=220,height=220)

        b1_1=Button(f_lbl_img,text="Train Data",cursor="hand2",command=self.train_data,font=("times new roman",15,"bold"),bg="#000000",fg="white")
        b1_1.place(x=200,y=600,width=220,height=40)

         # Photos
        img12=Image.open(r"images\18.jpg")
        img12=img12.resize((255,220),Image.ANTIALIAS)
        self.photoimg12=ImageTk.PhotoImage(img12)

        b1=Button(f_lbl_img,image=self.photoimg12,cursor="hand2",command=self.open_img)
        b1.place(x=500,y=400,width=220,height=220)

        b1_1=Button(f_lbl_img,text="Photos",cursor="hand2",command=self.open_img,font=("times new roman",15,"bold"),bg="#000000",fg="white")
        b1_1.place(x=500,y=600,width=220,height=40)

         # Developer
        img13=Image.open(r"images\43.jpg")
        img13=img13.resize((255,220),Image.ANTIALIAS)
        self.photoimg13=ImageTk.PhotoImage(img13)

        b1=Button(f_lbl_img,image=self.photoimg13,cursor="hand2",command=self.developer_data)
        b1.place(x=800,y=400,width=220,height=220)

        b1_1=Button(f_lbl_img,text="Developer",cursor="hand2",command=self.developer_data,font=("times new roman",15,"bold"),bg="#000000",fg="white")
        b1_1.place(x=800,y=600,width=220,height=40)

         # Exit
        img14=Image.open(r"images\46.jpg")
        img14=img14.resize((255,220),Image.ANTIALIAS)
        self.photoimg14=ImageTk.PhotoImage(img14)

        b1=Button(f_lbl_img,image=self.photoimg14,cursor="hand2",command=self.exit_page,)
        b1.place(x=1100,y=400,width=220,height=220)

        b1_1=Button(f_lbl_img,text="Exit",cursor="hand2",command=self.exit_page,font=("times new roman",15,"bold"),bg="#000000",fg="white")
        b1_1.place(x=1100,y=600,width=220,height=40)


        # ==============Functions Button================

    # for student_details button
    def student_details(self):
        self.new_window=Toplevel(self.root)
        self.app=Student(self.new_window)

    # for train button
    def train_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Train(self.new_window)

    # for Photos button
    def open_img(self):
        os.startfile("Data") 

    # for face_recognition button
    def face_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Face_Recognition(self.new_window)   

    # for attendance_data button
    def attendance_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Attendance(self.new_window)

    # for developer button
    def developer_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Developer(self.new_window)  

    # for help button
    def help_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Helpsupport(self.new_window)   

    # exit 
    def exit_page(self):
        self.exit_page=tkinter.messagebox.askyesno("Face Recognition","Are you sure to exit this software?",parent=self.root)    
        if self.exit_page > 0:
            self.root.destroy()
        else:
            return        


                

if __name__=="__main__":
    root=Tk()
    obj=Face_Recognition_System(root)
    root.mainloop()
        


