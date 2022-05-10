import ctypes
ctypes.windll.user32.MessageBoxW(0, "Your text", "Your title", 1)

import tkinter as tk
root = tk.Tk()
root.title("My GUI")
root.geometry("300x200")
root.mainloop()

import tkinter as tk
root = tk.Tk()
root.geometry("300x200")
root.title("My GUI")

# Create a Label
my_label = tk.Label(root, text="Hello World")
my_label.pack()
root.mainloop()

import tkinter as tk
root = tk.Tk()
root.geometry("300x200")
root.title("My GUI")

# Create a Label
my_label = tk.Label(root, text="Hello World", fg="red")
my_label.pack()

# Create a button
my_button = tk.Button(root, text="Click Me")
my_button.pack()

root.mainloop()

import tkinter as tk
root
