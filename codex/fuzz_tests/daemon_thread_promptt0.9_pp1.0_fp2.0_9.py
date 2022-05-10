import threading
# Test threading daemon, and tkinter

#import threading
import Queue
#import time

import tkinter as tk

class A:
    def __init__(self, n):
        self.n = n
    def __str__(self):
        return "<A(%d)>" % self.n
        
class FooApp(object):
    def __init__(self, master):
        self.master = master
        self.label = tk.Label(master, text="Working...")
        self.label.pack()
        self.calling_back()

    def calling_back(self):
        result = self.handler_thread.get_result() # block
        if result is None:
            self.master.after(100, self.calling_back)
        else:
            print("This is a callback in the mainthread. result: %s" % result)
            self.label["text"] = "Done"
        
    def run(self):
        self.handler_thread = Executor(FooHandler(self))
        self.handler_thread.start()
