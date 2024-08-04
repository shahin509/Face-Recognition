from multiprocessing import current_process
from tkinter import*
from tkinter import ttk
from turtle import bgcolor, position, width
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import cv2
import numpy as np
import os
import face_recognition
# import time
# from datetime import datetime




class Train:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition System")
        self.root.wm_iconbitmap("face.ico")


        title_lbl=Label(self.root,text="TRAIN DATA SET",font=("times new roman",35,"bold"),bg="#1b1717",fg="#989898")
        title_lbl.place(x=0,y=0,width=1530,height=45)

        ####   img_top  
        img_top=Image.open(r"images\54.jpg")
        img_top=img_top.resize((1530,325),Image.ANTIALIAS)
        self.photoimg_top=ImageTk.PhotoImage(img_top)

        f_lbl=Label(self.root,image=self.photoimg_top)
        f_lbl.place(x=0,y=55,width=1530,height=325)

        ### train button
        b1_1=Button(self.root,text="TRAIN DATA",command=self.train_classifier,cursor="hand2",font=("times new roman",30,"bold"),bg="#000000",fg="white")
        b1_1.place(x=0,y=380,width=1530,height=60)

        ##########    img_bottom 
        img_bottom=Image.open(r"images\62.jpg")
        img_bottom=img_bottom.resize((1530,325),Image.ANTIALIAS)
        self.photoimg_bottom=ImageTk.PhotoImage(img_bottom)

        f_lbl=Label(self.root,image=self.photoimg_bottom)
        f_lbl.place(x=0,y=440,width=1530,height=325)




    ###########      Training process         ##############
    def train_classifier(self):
        data_dir=("Data")
        path=[os.path.join(data_dir,file) for file in os.listdir(data_dir)]    

        faces=[]
        ids=[]

        for image in path:
            img=Image.open(image).convert('L')   #Grid scale image
            imageNp=np.array(img,'uint8')    

            id=int(os.path.split(image)[1].split('.')[1])

     
            faces.append(imageNp)
            ids.append(id)
            cv2.imshow("Training",imageNp)
            cv2.waitKey(1)==13
            
        ids=np.array(ids)

        #########  Train the classifier and save  ###########

        clf=cv2.face.LBPHFaceRecognizer_create()  
        clf.train(faces,ids)
        clf.write("classifier.xml")
        cv2.destroyAllWindows()
        messagebox.showinfo("Result","Training data sets completed!!")    








if __name__=="__main__":
    root=Tk()
    obj=Train(root)
    root.mainloop()
                