import tkinter
import threading
import winsound
import asyncio
wndw = tkinter.Tk()
lbl = tkinter.Label(
    text="Hello, Tkinter",
    fg="white",
    bg="black",
    width=20,
    height=2
)

a = 0
import threading
def pomodoro():
    global a
    a = a+1
    if ((a%8)==0):
        b=threading.Timer(3,pomodoro)
        print('longbreak')
        b.start()
    elif ((a%2)==0):
        b=threading.Timer(3,pomodoro)
        print('shortbreak')
        b.start()
    else:
        b=threading.Timer(3,pomodoro)
        print('pomodoro')
        b.start()

strtbtn= tkinter.Button(wndw, text="20", command= pomodoro)


lbl.pack()
strtbtn.pack()
wndw.mainloop()