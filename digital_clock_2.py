# from tkinter import Tk
from tkinter import *
import time

root=Tk()
root.title("CLOCK")
root.geometry("359x150+0+0")

root.configure(background="black")
root.resizable(0,0)

root.overrideredirect(0)

def start():
    text=time.strftime("%I:%M:%S:%p")
    label.config(text=text)
    label.after(200,start)
label=Label(root,font=("ds-digital",30,'bold'),bg='black',fg='red',bd=50)
label.grid(row=0,column=1)

start()
print("done")
root.mainloop()
