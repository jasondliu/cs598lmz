import ctypes
ctypes.windll.user32.MessageBoxW(0, "Hello World", "Hi", 1)

# Enable the below code to create a new window with a button.
# from tkinter import *
# window = Tk()
# button = Button(window, text="Click Me")
# button.pack()
# window.mainloop()
