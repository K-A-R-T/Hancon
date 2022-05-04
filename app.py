# Import required Libraries
from gzip import READ
from multiprocessing.spawn import prepare
from tkinter import *
import tkinter
from tokenize import String
from PIL import Image, ImageTk
import cv2
from cv2 import exp
import app_backend
import os

HEIGHT =  600
WIDTH = 500

# Create an instance of TKinter Window or frame
win = Tk()
win.title("Hancon")

can1 = Canvas(win, height=HEIGHT, width=WIDTH)
background_img = PhotoImage(file='D:/hancon_backend/aqua.png')
background_label = Label(win, image=background_img)
background_label.place(x=0,y=0,relwidth=1,relheight=1)
can1.place(relx=0,rely=1,relwidth=1,relheight=1)

#can1 = Canvas()
# Set the size of the window
win.geometry("600x500")

# Create a Label to capture the Video frames
def create_cam():
    label = Label(win)
    label.place(relx=0.5, rely=0.1, relwidth=0.7, relheight=0.6, anchor='n')
    return label
cap = cv2.VideoCapture(0)

def destroy_comp():
    b1.destroy()
    w.destroy()
    #msg.destroy()
def create_comp():
    lower_frame = Frame(win, bg='#42c2f4', bd=10)
    lower_frame.place(relx=0.5, rely=0.75, relwidth=0.7, relheight=0.2, anchor='n')
    bg_color = 'white'
    results = Label(lower_frame, anchor='nw', justify='left', bd=4)
    results.config(font=40, bg=bg_color)
    results.place(relwidth=1, relheight=1)
# Define function to show frame
nn = app_backend.prepare_model()


def show_frames():
    # Get the latest frame and convert into Image
    destroy_comp()
    #create_comp()
    label = create_cam()
    cv2image = cv2.cvtColor(cap.read()[1], cv2.COLOR_BGR2RGB)
    get_preds = app_backend.get_predictions(cv2image, nn)
    if get_preds == 'Restart':
        os.system("shutdown /r /t 1")
    else:
        app_backend.map_to_keyboard(get_preds) 
    #label['text'] = str(643)
    img = Image.fromarray(cv2image)
    # Convert image to PhotoImage
    imgtk = ImageTk.PhotoImage(image=img)
    label.imgtk = imgtk
    label.configure(image=imgtk)
    # Repeat after an interval to capture continiously
    label.after(20, show_frames)
    

b1 = Button(win, text="click me!",command=show_frames)
b1.place(relx=0.5, rely=0.2, relwidth=0.1, relheight=0.1, anchor='n')
w = Label(win, text='Welcome to HANCON!',font="90",fg="Navyblue")
w.place(relx=0.5, rely=0.1,anchor='n')
#msg = Message(win,text="Click the button to start the application...")
#msg.place(relx=0.5, rely=0.5,anchor='n')

win.mainloop()





