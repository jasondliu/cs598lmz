import ctypes
ctypes.windll.user32.MessageBoxW(0, "Hello World", "My first GUI Python program", 1)

# import tkinter as tk
# from tkinter import ttk
#
# root = tk.Tk()
# root.title("Hello World")
# root.geometry("200x100")
#
# label = ttk.Label(root, text="Hello World")
# label.grid(row=0, column=0, columnspan=2)
#
# button1 = ttk.Button(root, text="Click Me")
# button1.grid(row=1, column=0)
#
# button2 = ttk.Button(root, text="Exit")
# button2.grid(row=1, column=1)
#
# root.mainloop()
