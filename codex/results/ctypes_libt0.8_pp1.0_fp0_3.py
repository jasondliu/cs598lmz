import ctypes
ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID("myappid")
def center(toplevel):
    toplevel.update_idletasks()
    w = toplevel.winfo_screenwidth()
    h = toplevel.winfo_screenheight()
    size = tuple(int(_) for _ in toplevel.geometry().split('+')[0].split('x'))
    x = w/2 - size[0]/2
    y = h/2 - size[1]/2
    toplevel.geometry("%dx%d+%d+%d" % (size + (x, y)))

tk = Tk()
tk.title("Awnser")
center(tk)

text = scrolledtext.ScrolledText(tk, wrap=WORD, width=100, height=100)
text.pack()

def load(file="aw2.txt"):
    with open(file, "r") as f:
        text.delete('1.0', END)
        text.insert('1.
