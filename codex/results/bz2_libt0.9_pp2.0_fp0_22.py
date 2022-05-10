import bz2
bz2_file = bz2.BZ2File('test.asm.bz2')
bz2_file.read().decode('utf-8')

# os.system('c:\\Users\\admin\\Desktop\\test.bat')

# tkinter
print("tkinter")
import tkinter
from tkinter import *

wnd = tkinter.Tk()
wnd.title("Demo windows")
def onClick():
    lbl2['text'] = 'Button clicked.'

lbl = tkinter.Label(wnd, text="Hello, World!")
lbl.grid(row=0, column=0, columnspan=10)
lbl2 = tkinter.Label(wnd, text='')
lbl2.grid(row=1, column=0, columnspan=10)
btn = tkinter.Button(wnd, text="Click Me!", command=onClick)
btn.grid(row=2, column=0)
txt = tkinter.Entry(wnd,width=10)
txt.grid(row
