import ctypes
ctypes.windll.user32.MessageBoxW(0, "Your text", "Your title", 1)

def hello(event):
    print("Single Click, Button-l") 

def quit(event):
    print("Double Click, so let's stop")
    import sys; sys.exit()

frame = Frame(root, width=300, height=250)
frame.bind("<Button-1>", hello)
frame.bind("<Double-1>", quit)
frame.pack()

root.mainloop()
