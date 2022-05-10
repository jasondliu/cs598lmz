import ctypes
ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID("myappid")

root = Tk()
root.geometry("450x300+400+300")

def hello():
    print("hello!")

app = Frame(root)
app.grid()

b1 = Button(app, text="Print something", command=hello)
b1.grid()

b2 = Button(app, text="Quit", command=root.destroy)
b2.grid()

root.mainloop()
</code>

