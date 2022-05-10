import ctypes
ctypes.windll.user32.MessageBoxW(0, "Your text", "Your title", 1)

#https://www.geeksforgeeks.org/python-gui-tkinter/

from tkinter import *
from tkinter import messagebox

# create the root window
root = Tk()

# modify the window
root.title("GUI")
root.geometry("200x100")

# kick off the window's event-loop
root.mainloop()

#https://www.geeksforgeeks.org/python-gui-tkinter/

from tkinter import *
from tkinter import messagebox

# create the root window
root = Tk()

# modify the window
root.title("GUI")
root.geometry("200x100")

def helloCallBack():
   messagebox.showinfo("Hello Python", "Hello World")

# creating a button instance
B = Button(root, text = "Hello", command = helloCallBack)

# placing the button on my window
B.place(x = 50,y = 50)

