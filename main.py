import threading #for thread
import tkinter #for window GUI
import winsound #for beep sound (works in windows OS only)

#note: a trailing underscore is used in identifieres

window_ = tkinter.Tk()  #create windows object
label_ = tkinter.Label(   #display box
    text="press start to start pomodoro",
    fg="white",
    bg="black",
    width=20,
    height=2,
    padx=10
)

counter_ = 0
#the only counter in this program.long-short breaks and pomodoros are all based on this counter

def pomodoro_():

    winsound.PlaySound("SystemExit", winsound.SND_ALIAS)
    global counter_
    counter_ = counter_ + 1
    # => Beep and counter increment in each recursive function calls

        #long break
    if (counter_ % 8)==0:  #after every 4th pomodoro work
        long_break_=threading.Timer(1200, pomodoro_)  #20 minutes break
        long_break_.daemon=True  #daemon-threads gets killed when sys.exit()
        long_break_.start()

        #short break
    elif (counter_ % 2) == 0:  #after every pomodoro work except those which are not four's multiples
        long_break_=threading.Timer(300, pomodoro_)  #5 minutes break
        long_break_.daemon = True  #daemon-threads gets killed when sys.exit()
        long_break_.start()

        #pomodoro
    else:
        label_.config(text=int((counter_ / 2) + .5))  #equation to subract all breaks from counter
        long_break_=threading.Timer(1500, pomodoro_)  #25 minutes
        long_break_.daemon = True
        long_break_.start()



start_button_= tkinter.Button( window_, text="Start", command= pomodoro_)
#startbutton that inititiates pomodoro()

#place widgets in the window
label_.pack()
start_button_.pack()

window_.mainloop()
#infinitely loops(till closed) the window_ object, listens events.refer python documentation for working


#MVP
#primary:make a non daemon thread to store data if window is closed
#make string along with numbercount
#make a custom louder sound that supports everywhere
#secondary:make a stop function to kill the daemon pomodoro thread without closing window