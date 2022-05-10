import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect()
L = []
for i in range(100):
    L = [i]
    L[:0] = L
    L = [L,L]
    L[:] = L
    # this will take as long as it can, but after 2 or 3 seconds,
    # the app should become responsive again
    gc.collect()
gc.collect()
from tkinter import *
from tkinter.simpledialog import askstring
from tkinter.filedialog   import asksaveasfilename


class Quitter(Frame):                         # subclass our GUI
    def __init__(self, parent=None):           # constructor method
        Frame.__init__(self, parent)
        self.pack()
        widget = Button(self, text='Quit', command=self.quit)
        widget.pack(side=LEFT, expand=YES, fill=BOTH)

    def quit(self):
        ans = askstring('Verify quit', 'Are you sure you want to quit?')
        if ans == 'yes': Frame.quit(self)


class Scrolled
