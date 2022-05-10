import ctypes
ctypes.windll.user32.MessageBoxA(0, "Your text", "Your title", 1)
import tkinter as tk
from tkinter import messagebox
root = tk.Tk()
root.withdraw()
messagebox.showerror("Error", "Error message")
from tkinter import *
import subprocess
top = Tk()
def helloCallBack():
   subprocess.call(['notepad.exe', 'error.txt'])
B = Button(top, text ="Hello", command = helloCallBack)
B.pack()
top.mainloop()
import os
import subprocess
subprocess.call(['notepad.exe', 'error.txt'])
import os
os.system('notepad.exe error.txt')
import os
os.system('notepad.exe error.txt')
import os
os.startfile('error.txt')
import os
os.startfile('error.txt')
import os
os.startfile('error.txt')
import os
os.startfile('error.txt')
import os
os.startfile
