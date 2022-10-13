import tkinter
from time import sleep
wndw = tkinter.Tk()
lbl = tkinter.Label(
    text="Hello, Tkinter",
    fg="white",
    bg="black",
    width=20,
    height=2
)
i=0
j=0
def startcount():
    global i,j
    while(i<2):
        i=i+1
        wndw.after(600,startcount())
        j=j+1
        def startcountbreak():
            wndw.after(6000, startcount())

lbl.config(font=('Helvatical bold',20))

strtbtn= tkinter.Button(wndw, text="20", command= startcount)
strtbtn.pack(pady=10)
#stpbtn= tkinter.button(wndw, text="stop", command=stopcount())
#stpbtn.pack(pady=10)

lbl.pack()
wndw.mainloop()