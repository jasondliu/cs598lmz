import sys, threading
threading.Thread(target=lambda:sys.stdout.write('\\'*1200000)).start()
try:
    from Tkinter import *
except ImportError:
    from tkinter import *



class App1(Frame):
    def __init__(self, master):
        Frame.__init__(self, master)
        self.pack()
        self.master.title("App 1")


class App2(Frame):
    def __init__(self, master):
        Frame.__init__(self, master)
        self.pack()
        self.master.title("App 2")


class App3(Frame):
    def __init__(self, master):
        Frame.__init__(self, master)
        self.pack()
        self.master.title("App 3")


class App4(Frame):
    def __init__(self, master):
        Frame.__init__(self, master)
        self.pack()
        self.master.title("App 4")

