import ctypes
ctypes.windll.user32.MessageBoxW(0, "Your text", "Your title", 1)

import tkinter as tk
from tkinter import messagebox

root = tk.Tk()
root.withdraw()

messagebox.showinfo("Title", "a Tk MessageBox")

#import tkMessageBox
#tkMessageBox.showinfo("Title", "a Tk MessageBox")

#import tkMessageBox
#tkMessageBox.showinfo(title="Title", message="a Tk MessageBox")

#import tkMessageBox
#tkMessageBox.showinfo(title="Title", message="a Tk MessageBox", detail="More details")

#import tkMessageBox
#tkMessageBox.showinfo(title="Title", message="a Tk MessageBox", detail="More details", icon="warning")

#import tkMessageBox
#tkMessageBox.showinfo(title="Title", message="a Tk MessageBox", detail="More details", icon="warning", type="okcancel")

#import tkMessageBox
#tkMessage
