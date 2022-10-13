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

def waitThis():
    frequency = 1000 # Set Frequency To 2500 Hertz
    duration = 200  # Set Duration To 1000 ms == 1 second
    winsound.PlaySound("SystemQuestion", winsound.SND_ALIAS)
class customthread:
    def __init__(self):
        threading.Timer(1500, waitThis)
async def startaction():
    pomodorotimer=threading.Timer(1500,waitThis)
    shortbreaktimer=threading.Timer(300,waitThis)
    longbreaktimer=threading.Timer(1200,waitThis)
    a= pomodorotimer.start()
    lbl.config(font=('Helvatical bold',20))

strtbtn= tkinter.Button(wndw, text="20", command= startaction)


lbl.pack()
strtbtn.pack()
wndw.mainloop()