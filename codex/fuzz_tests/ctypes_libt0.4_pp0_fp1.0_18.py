import ctypes
ctypes.windll.user32.MessageBoxW(0, "Your text", "Your title", 1)

#%%
# import tkinter as tk
# from tkinter import messagebox

# root = tk.Tk()
# root.withdraw()

# messagebox.showinfo("Title", "a Tk MessageBox")

#%%
import tkinter as tk
import tkinter.messagebox

root = tk.Tk()
root.withdraw()

tkinter.messagebox.showinfo("Title", "a Tk MessageBox")
