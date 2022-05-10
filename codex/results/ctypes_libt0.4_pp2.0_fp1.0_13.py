import ctypes
ctypes.windll.user32.MessageBoxW(0, "Your text", "Your title", 1)

#%%
import tkinter as tk
from tkinter import messagebox

root = tk.Tk()
root.withdraw()

messagebox.showinfo("Title", "a Tk MessageBox")

#%%
import tkinter as tk

root = tk.Tk()

w = tk.Label(root, text="Hello Tkinter!")
w.pack()

root.mainloop()

#%%
import tkinter as tk

root = tk.Tk()

v = tk.IntVar()

tk.Label(root, 
        text="""Choose a 
programming language:""",
        justify = tk.LEFT,
        padx = 20).pack()
tk.Radiobutton(root, 
              text="Python",
              padx = 20, 
              variable=v, 
              value=1).pack(anchor=tk.W)
tk.Radi
