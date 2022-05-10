import ctypes
ctypes.windll.kernel32.SetConsoleTitleW("Python Tkinter Scale")
from tkinter import *

root = Tk()
root.geometry("400x250")
root.title("Python Tkinter Scale")

def scale():
    my_label = Label(root, text=click_value.get()).pack()

click_value = DoubleVar()
show_scale = Scale(root, orient=HORIZONTAL, length=300, width=20, sliderlength=25,
                   from_=0, to=25, tickinterval=5, resolution=5, command=scale,
                   variable=click_value).pack()

my_button = Button(root, text="ok", command=scale).pack()

root.mainloop()
