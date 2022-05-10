import ctypes
ctypes.windll.user32.MessageBoxW(0, "Your text", "Your title", 1)

import tkinter as tk
from tkinter import messagebox

# show info dialog
messagebox.showinfo("Title", "a Tk MessageBox")

# show warning dialog
messagebox.showwarning("Warning", "A Warning Message")

# show error dialog
messagebox.showerror("Error", "An Error Message")

# ask question
messagebox.askquestion("Question", "Are you sure?")

# ask yes/no
messagebox.askyesno("Question", "Are you sure?")

# ask ok/cancel
messagebox.askokcancel("Question", "Continue?")

# ask retry/cancel
messagebox.askretrycancel("Question", "Try again?")

# ask yes/no/cancel
messagebox.askyesnocancel("Question", "Continue?")

# ask yes/no/cancel
messagebox.askyesnocancel("Question", "Continue?")

# ask yes/no/c
