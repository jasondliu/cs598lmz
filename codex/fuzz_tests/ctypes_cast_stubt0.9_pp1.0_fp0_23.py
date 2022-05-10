import ctypes
ctypes.cast(id(rob.recall_current_context()), ctypes.py_object).value
 
 
 
main=Tk()
main.geometry("150x150")
def helper():
    return Label(main, text='Press OK when done')
 
a=helper()
def hello():
    a.pack()
 
 
b=Button(main, text='click here', command=hello)
b.pack()
c=Button(main, text='quit', command=main.destroy)
c.pack()


 
main.mainloop()
