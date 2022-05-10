import ctypes
ctypes.windll.user32.MessageBoxW(0, "Your text", "Your title", 1)

#from tkinter import messagebox
#messagebox.showinfo("Title", "a Tk MessageBox")

#from tkinter import *
#import tkinter as tk
#win = tk.Tk()
#win.title("Python GUI")
#win.mainloop()

#import tkinter as tk
#from tkinter import ttk
#win = tk.Tk()
#win.title("Python GUI")
#ttk.Label(win, text="A Label").grid(column=0, row=0)
#win.mainloop()

#import tkinter as tk
#from tkinter import ttk
#win = tk.Tk()
#win.title("Python GUI")
#aLabel = ttk.Label(win, text="A Label")
#aLabel.grid(column=0, row=0)
#def clickMe():
#    action.configure(text='Hello ' + name.get())
