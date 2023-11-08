from cgitb import text
from decimal import BasicContext
from itertools import filterfalse
from mailbox import mboxMessage
from string import whitespace
from tkinter import*
from tkinter import Label
import time 
import sys
from tkinter import messagebox

import tkinter as tk

  

import tkinter as tk


running = False

hours, minutes, seconds = 0, 0, 0


root = Tk()
root.title("Timer")
root.geometry("400x600")
root.config(bg="white")
root.resizable(False,False)




heading=Label(root,text="นาฬิกา",font="arial 30 bold",bg="white",fg="blue")
heading.pack(pady=10)


Label(root,font=("arial",15,"bold"),text="เวลาปัจจุบัน:",bg="gray",fg="white").place(x=65,y=70)

def clock():
    clock_time=time.strftime('%H:%M:%S %p')
    current_time.config(text=clock_time)
    current_time.after(1000,clock)

current_time = Label(root,font=("arial",15,"bold"),text="",fg="white",bg="gray")
current_time.place(x=190,y=70)
clock()

#timer
hrs=StringVar()
Entry(root,textvariable=hrs,width=2,font="arial 50").place(x=30,y=155)
hrs.set("00")

mins=StringVar()
Entry(root,textvariable=mins,width=2,font="arial 50").place(x=150,y=155)
mins.set("00")

sec=StringVar()
Entry(root,textvariable=sec,width=2,font="arial 50").place(x=270,y=155)
sec.set("00")

Label(root,text="hours",font="arial 12",bg="white",fg="black").place(x=105,y=200)
Label(root,text="mins",font="arial 12",bg="white",fg="black").place(x=225,y=200)
Label(root,text="sec",font="arial 12",bg="white",fg="black").place(x=345,y=200)

def start():
    global running
    if not running:
        update()
        running = True


def pause():
    global running
    if running:

        stopwatch_label.after_cancel(update_time)
        running = False

def reset():
    global running
    if running:

        stopwatch_label.after_cancel(update_time)
        running = False

    global hours, minutes, seconds
    hours, minutes, seconds = 0, 0, 0

    stopwatch_label.config(text='00:00:00')


def update():

    global hours, minutes, seconds
    seconds += 1
    if seconds == 60:
        minutes += 1
        seconds = 0
    if minutes == 60:
        hours += 1
        minutes = 0

    hours_string = f'{hours}' if hours > 9 else f'0{hours}'
    minutes_string = f'{minutes}' if minutes > 9 else f'0{minutes}'
    seconds_string = f'{seconds}' if seconds > 9 else f'0{seconds}'

    stopwatch_label.config(text=hours_string + ':' + minutes_string + ':' + seconds_string)

    global update_time
    update_time = stopwatch_label.after(1000, update)

def Timer():
    times=int(hrs.get())*3600 +int(mins.get())*60+int(sec.get())
    
    while times > -1:
        minute ,second=(times//60,times %60)
        
        hour=0
        if minute>60:
            hour,minute=(minute//60,minute%60)

        sec.set(second)
        mins.set(minute)
        hrs.set(hour)

        root.update()
        time.sleep(1)

        if(times == 0):
            messagebox.showinfo("","หมดเวลา!")

        

        times -= 1
botton1 = Button(root,text="เริ่ม",fg="white",bg="blue",width=20,height=2,font="arial 10 bold",command=Timer).place(x=120,y=250)




stopwatch_label = tk.Label(root,text='00:00:00', font=('Arial',70),bg="white",fg="black")
stopwatch_label.place(x=15,y=350)

start_button = tk.Button(root,text="เริ่ม",fg="white",bg="blue",width=10,height=2,font="arial 10 bold", command=start)
start_button.place(x=0,y=500)
pause_button = tk.Button(root,text="หยุด",fg="white",bg="blue",width=10,height=2,font="arial 10 bold", command=pause)
pause_button.place(x=100,y=500)
reset_button = tk.Button(root,text="รีเซ็ต",fg="white",bg="blue",width=10,height=2,font="arial 10 bold", command=reset)
reset_button.place(x=200,y=500)
quit_button = tk.Button(root,text="ออก",fg="white",bg="blue",width=10,height=2,font="arial 10 bold", command=root.quit)
quit_button.place(x=300,y=500)


mainloop()
