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
def pomodoro():

    winsound.PlaySound("SystemExit", winsound.SND_ALIAS)
    global a
    a = a+1

    if ((a%8)==0):
        b=threading.Timer(3,pomodoro)
        b.daemon=True
        print('longbreak')
        b.start()
    elif ((a%2)==0):
        b=threading.Timer(3,pomodoro)
        b.daemon = True
        print('shortbreak')
        b.start()
    else:
        lbl.config(text=int((a/2)+.5) )#just an eqn to subract the no. of breaks from global variable
        b=threading.Timer(3,pomodoro)
        b.daemon = True #daemon-threads gets killed when sys.exit()
        print('pomodoro')
        b.start()
#MVP
#primary:make a non daemon thread to store data if window is closed
#make string along with number
#make a custom louder sound that supports everywhere
#secondary:make a stop function to kill the daemon pomodoro thread without closing window
strtbtn= tkinter.Button(wndw, text="Start", command= pomodoro)


lbl.pack()
strtbtn.pack()
wndw.mainloop()