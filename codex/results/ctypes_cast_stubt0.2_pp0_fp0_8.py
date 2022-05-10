import ctypes
ctypes.cast(0, ctypes.py_object)

# imports for Python3
try:
    import tkinter
except ImportError:
    import Tkinter as tkinter

# imports for Python2
# import Tkinter as tkinter

print(tkinter.TkVersion)
print(tkinter.TclVersion)

# tkinter._test()

mainWindow = tkinter.Tk()

mainWindow.title("Hello World")
mainWindow.geometry('640x480+8+400')

label = tkinter.Label(mainWindow, text="Hello World")
label.pack(side='top')

canvas = tkinter.Canvas(mainWindow, relief='raised', borderwidth=1)
canvas.pack(side='left', fill=tkinter.BOTH, expand=True)

mainWindow.mainloop()
