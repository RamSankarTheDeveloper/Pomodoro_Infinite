import tkinter
import threading
wndw = tkinter.Tk()
lbl = tkinter.Label(
    text="Hello, Tkinter",
    fg="white",
    bg="black",
    width=20,
    height=2
)

def startcount():
    print("nothing")

lbl.config(font=('Helvatical bold',20))

strtbtn= tkinter.Button(wndw, text="20", command= startcount)


lbl.pack()
strtbtn.pack()
wndw.mainloop()