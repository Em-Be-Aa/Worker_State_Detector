# This program has the basic purpose of observing and displaying the state
# of the person working in a video or camera and has some widgets in the GUI
# for some other necessary information.


# Here we import some of the libraries needed for the computation done afterwards.

import cv2
import random
import mediapipe as mp
import numpy as np
import time
from tkinter import *
from PIL import Image, ImageTk
import tkinter.font as font



# This is the function used to convert x and y axis points to degrees.

def calculate_angle(a,b,c):
        a=np.array(a)
        b=np.array(b)
        c=np.array(c)

        radians= np.arctan2(c[1]-b[1], c[0]-b[0]) - np.arctan2(a[1]-b[1],a[0]-b[0])
        angle = np.abs(radians*180.0/np.pi)
        if angle >180.0:
            angle=360-angle
        return angle

# These all functions are used as a toggle for displaying important data on window.

def myFunc7():
    global sho1 ,is_on
    sho1+=1

    if sho1%2==0:
        myButton7.config(image=on)
        is_on=True
    else:
        myButton7.config(image=off)
        is_on=False


def myFunc8():
    global sho2,is_on
    sho2+=1
    if sho2%2==0:
        myButton8.config(image=on)
        is_on=True
    else:
        myButton8.config(image=off)
        is_on=False


def myFunc9():
    global sho3,is_on
    sho3+=1
    if sho3%2==0:
        myButton9.config(image=on)
        is_on=True
    else:
        myButton9.config(image=off)
        is_on=False


def myFunc10():
    global sho4,is_on
    sho4+=1
    if sho4%2==0:
        myButton10.config(image=on)
        is_on=True
    else:
        myButton10.config(image=off)
        is_on=False


def myFunc11():
    global sho5,is_on
    sho5+=1
    if sho5%2==0:
        myButton11.config(image=on)
        is_on=True
    else:
        myButton11.config(image=off)
        is_on=False


def myFunc12():
    global sho6,is_on
    sho6+=1
    if sho6%2==0:
        myButton12.config(image=on)
        is_on=True
    else:
        myButton12.config(image=off)
        is_on=False


def myFunc13():
    root.destroy()

# This function randomize the colors of the heading.

def color_changer():
    fg = random.choice(colors)
    myLabel7.config(fg = fg)
    myLabel7.after(200, color_changer)


# This module uses mediapipe for importing google solution for body points of a human.

mp_drawing=mp.solutions.drawing_utils
mp_pose=mp.solutions.pose

# This function is used to capture different videos and live camera.

cap1=cv2.VideoCapture("Video 1.mp4")
cap2=cv2.VideoCapture('Video 2.mp4')
cap3=cv2.VideoCapture('Video 3.mp4')
cap4=cv2.VideoCapture('Video 4.mp4')
cap5=cv2.VideoCapture('Video 5.mp4')
cap6=cv2.VideoCapture(0)

# Initialization of different driving variables for the module.

ttime=0
movement=0
idle=0
ptime=0
ctime=0
counter=0
stage=None
cycle=0
a=1
sho1,sho2,sho3,sho4,sho5,sho6=1,1,1,1,1,1
cp1,cp2,cp3,cp4,cp5,cp6=0,0,0,0,0,0
w = 1080
h = 600
options=["Camera" , "V1.mp4" , "V2.mp4" , "V3.mp4" , "V4.mp4" , "V5.mp4"]
colors = ["red" , "yellow",'orange']

 
# Making the Tkinter window for video to diplay

root=Tk()
root.geometry('1920x1080')


# Images for different buttons on the Tkinter window.

on = PhotoImage(file = "on.png")
off = PhotoImage(file = "off.png")
power=PhotoImage(file="power.png")
font1=font.Font(family="Agency FB", size=15, weight="bold")
font2=font.Font(family="Agency FB", size=25, weight="bold")

# Making labels for the video and for the title of the window.


frame_1 = Frame(root, width=1280, height=720, bg="black").place(x=0, y=0)
myLabel8= Label(frame_1, width=w, height=h)
myLabel8.place(x=100, y=50)



myLabel7= Label(root, text="WORKER STATE PROGRAM", bg="black")
myLabel7.config(font=font2)
myLabel7.pack()
# Buttons for toogling the information displayed on the screen and an Exit button.

myButton7=Button(root,image=off,padx=30,pady=10,fg='red',command=myFunc7, width=55,height=25)
myButton7.place(x=10,y=100)
myButton8=Button(root,image=off,padx=30,pady=10,fg='red',command=myFunc8, width=55,height=25)
myButton8.place(x=10,y=200)
myButton9=Button(root,image=off,padx=30,pady=10,fg='red',command=myFunc9, width=55,height=25)
myButton9.place(x=10,y=300)
myButton10=Button(root,image=off,padx=30,pady=10,fg='red',command=myFunc10, width=55,height=25)
myButton10.place(x=10,y=400)
myButton11=Button(root,image=off,padx=30,pady=10,fg='red',command=myFunc11, width=55,height=25)
myButton11.place(x=10,y=500)
myButton12=Button(root,image=off,padx=30,pady=10,fg='red',command=myFunc12, width=55,height=25)
myButton12.place(x=10,y=600)
myButton13=Button(root,image=power,padx=30,pady=10,fg='red',bg='black',command=myFunc13, width=100,height=91)
myButton13.place(x=1185,y=15)

# Labels for the buttons described above.


myLabel1= Label(root, text = "WORK",font=font1,fg='red',bg='black').place(x = 17,y = 70) 
myLabel2= Label(root, text = "IDLE",font=font1,fg='red',bg='black').place(x = 21,y = 170) 
myLabel3= Label(root, text = "FPS",font=font1,fg='red',bg='black').place(x = 22,y = 270) 
myLabel4= Label(root, text = "CYCLE",font=font1,fg='red',bg='black').place(x = 17,y = 370) 
myLabel5= Label(root, text = "ANGLE",font=font1,fg='red',bg='black').place(x = 17,y = 470) 
myLabel6= Label(root, text = "%",font=font1,fg='red',bg='black').place(x = 24,y = 570) 

# Drop down menu to switch between videos.

clicked=StringVar()
clicked.set(options[1])
drop = OptionMenu(frame_1, clicked, *options).place(x=1185, y=250) 

# Calling the heading color changer function.

color_changer()
 
# This is the start of the while statement which will display the frames and it will take
# the shape of avideo due to its speed.

with mp_pose.Pose(min_detection_confidence=0.5, min_tracking_confidence=0.5) as pose:
    while True:

# if conditions to check for the change in drop down menu and switch the video
# and read statement will read one frame of the video captured.

        if clicked.get()=="V1.mp4":
            success, frame1= cap1.read()
            if success:
                frame1 = cv2.resize(frame1, (1080,650))
            if cp1==0:
                movement=1
                idle=1
                counter=0
                cp1+=1

        if clicked.get()=="V2.mp4":
            success, frame1= cap2.read()
            if success:
                frame1 = cv2.resize(frame1, (1080,650))
            if cp2==0:
                movement=1
                idle=1
                counter=0
                cp2+=1

        if clicked.get()=="V3.mp4":
            success, frame1= cap3.read()
            if success:
                frame1 = cv2.resize(frame1, (1080,650))
            if cp3==0:
                movement=1
                idle=1
                counter=0
                cp3+=1

        if clicked.get()=="V4.mp4":
            success, frame1= cap4.read()
            if success:
                frame1 = cv2.resize(frame1, (1080,650))
            if cp4==0:
                movement=1
                idle=1
                counter=0
                cp4+=1

        if clicked.get()=="V5.mp4":
            success, frame1= cap5.read() 
            if success:
                frame1 = cv2.resize(frame1, (1080,650)) 
            if cp5==0: 
                movement=1
                idle=1 
                counter=0    
                cp5+=1

        if clicked.get()=="Camera":
            success, frame1= cap6.read() 
            if success: 
                frame1 = cv2.resize(frame1, (1080,650))
            if cp6==0: 
                movement=1
                idle=1  
                counter=0   
                cp6+=1

# Statements to restart the video if the video ends by starting frames from 0.

        if success== False:
            if a==1:
                cap1.set(cv2.CAP_PROP_POS_FRAMES, 0)
                success, frame1=cap1.read()
                cp1=0
            if a==2:
                cap2.set(cv2.CAP_PROP_POS_FRAMES, 0)
                success, frame1=cap2.read()
                cp2=0
            if a==3:
                cap3.set(cv2.CAP_PROP_POS_FRAMES, 0)
                success, frame1=cap3.read()
                cp3=0
            if a==4:
                cap4.set(cv2.CAP_PROP_POS_FRAMES, 0)
                success, frame1=cap4.read()
                cp4=0
            if a==5:
                cap5.set(cv2.CAP_PROP_POS_FRAMES, 0)
                success, frame1=cap5.read()
                cp5=0
            if a==6:
                cap6.set(cv2.CAP_PROP_POS_FRAMES, 0)
                success, frame1=cap6.read()
                cp6=0

# Converting color scheme of the frame so that it is writeable
# and imposing the results.

        image=cv2.cvtColor(frame1, cv2.COLOR_BGR2RGB)
        image.flags.writeable = False
        results=pose.process(image)
                    
# Drawing the points on all the 33 points in google solution and connecting them all together.

        mp_drawing.draw_landmarks(image, results.pose_landmarks, mp_pose.POSE_CONNECTIONS,
                                  mp_drawing.DrawingSpec(color=(245,117,66), thickness=2, circle_radius=2), 
                                  mp_drawing.DrawingSpec(color=(245,66,230), thickness=2, circle_radius=2))

# Extracting the x and y points of shoulder, elbow and wrist of every frame by mediapipe
# and using them in angle finder function. if condition is used for checking the angle and
# and displaying working or idle according to the condition.

        try:
            
            landmarks = results.pose_landmarks.landmark
            shoulder= [landmarks[mp_pose.PoseLandmark.LEFT_SHOULDER.value].x, landmarks[mp_pose.PoseLandmark.LEFT_SHOULDER.value].y]
            elbow=  [landmarks[mp_pose.PoseLandmark.LEFT_ELBOW.value].x, landmarks[mp_pose.PoseLandmark.LEFT_ELBOW.value].y]
            wrist=  [landmarks[mp_pose.PoseLandmark.LEFT_WRIST.value].x, landmarks[mp_pose.PoseLandmark.LEFT_WRIST.value].y]
            
            angle= calculate_angle(shoulder, elbow, wrist)

            if angle<140:
                
                movement+=1
                
                cv2.putText(image, "State: {}".format('Working'), (500,50), cv2.FONT_HERSHEY_PLAIN,1,(0,0,255),3)

            else:
                
                idle+=1
                cv2.putText(image, "State: {}".format('Idle'), (500,60), cv2.FONT_HERSHEY_PLAIN,1,(0,0,255),3)
                

            
        except:
            cv2.putText(image, "State: {}".format('Idle'), (500,60), cv2.FONT_HERSHEY_PLAIN,1,(0,0,255),3)

# Finding different values of FPS, movement, idle and efficiency.

        ctime=time.time()
        fps=1/(ctime-ptime)
        ptime=ctime
        mov=movement/15
        idl=idle/15
        eff=(mov/(mov+idl))*100
        bar=np.interp(eff, (0,100),(650,100))


# Conditions to display all the above described values according to the toggle buttons.

        if sho3%2==0:
            cv2.putText(image, str(int(fps)),(95,50), cv2.FONT_HERSHEY_PLAIN,2, (255,0,0), 3)
            cv2.putText(image, format('FPS:'), (10,50), cv2.FONT_HERSHEY_PLAIN,2,(255,0,0),3)

        if sho1%2==0:
            cv2.putText(image,format('Working Time:'), (10,80), cv2.FONT_HERSHEY_PLAIN,1,(45,45,255),3)
            cv2.putText(image,str(int(mov)), (140,80), cv2.FONT_HERSHEY_PLAIN,1,(45,45,255),3)

        if sho2%2==0:
            cv2.putText(image,format('Idle Time:'), (10,105), cv2.FONT_HERSHEY_PLAIN,1,(45,45,255),3)
            cv2.putText(image,str(int(idl)), (140,105), cv2.FONT_HERSHEY_PLAIN,1,(45,45,255),3)   

        if sho4%2==0:
            cv2.putText(image,format('Cycles:'), (10,130), cv2.FONT_HERSHEY_PLAIN,1,(45,45,255),3)
            cv2.putText(image,str(int(counter)), (140,130), cv2.FONT_HERSHEY_PLAIN,1,(45,45,255),3)

        if sho5%2==0:
            cv2.putText(image,format('Angle:'), (10,155), cv2.FONT_HERSHEY_PLAIN,1,(45,45,255),3)
            cv2.putText(image,str(int(angle)), (140,155), cv2.FONT_HERSHEY_PLAIN,1,(45,45,255),3)

        if sho6%2==0:           
            cv2.putText(image,str(int(eff)), (1020,80), cv2.FONT_HERSHEY_PLAIN,2,(45,45,255),3)
            cv2.rectangle(image, (1020,100),(1060,650),(0,255,0),3)    
            cv2.rectangle(image, (1020,int(bar)),(1060,650),(0,255,0),cv2.FILLED)    
        
#  finding the counter or cycle of the worker.

        if angle > 170:
            stage = "down"
        if angle < 150 and stage =='down':
            stage="up"
            counter +=1

# Displaying the processed image on th Tkinter window

        image = ImageTk.PhotoImage(Image.fromarray(image))
        myLabel8['image']=image

# This function updates the window by continuing the while loop.

        root.update()

# End of Module.