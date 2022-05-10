import ctypes
ctypes.windll.user32.MessageBoxW(0, "Your text", "Your title", 1)
import ctypes
# MessageBox = ctypes.windll.user32.MessageBoxW
# MessageBox(None, 'Your text', 'Your title', 0)
root = Tk()

def hello():
    print("Hello World")
    ctypes.windll.user32.MessageBoxW(0, "Your text", "Your title", 1)

btn = Button(root, text = "Hello World", command = hello)

btn.pack()

root.mainloop()

# import ctypes
# ctypes.windll.user32.MessageBoxW(0, "Your text", "Your title", 1)

# import tkinter as tk
# from tkinter import messagebox

# root = tk.Tk()

# def hello():
#     messagebox.showinfo("Say Hello", "Hello World")

# button = tk.Button(root, text="Say Hello", command=hello)
# button.pack()

# root.mainloop
