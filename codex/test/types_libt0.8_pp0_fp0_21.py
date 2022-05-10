import types
types.FunctionType

frame = Frame()

def callback():
    print('hello')

btn = Button(frame, text='Click Me', command=callback)
btn.pack()

frame.mainloop()
