import ctypes
ctypes.windll.user32.MessageBoxW(0, "Your text", "Your title", 1)

import tkinter
tkinter.messagebox.showinfo("This is a Title", "This is the Message")

filename = 'data/text.txt'

# with open(filename, 'r') as f:
#     text = f.read()

# print(text)

text = '''
    The Zen of Python

    Beautiful is better than ugly.
    
    Explicit is better than implicit.
    
    Simple is better than complex.
    
    Complex is better than complicated.
    
    Flat is better than nested.
    
    Sparse is better than dense.
    
    Readability counts.
    
    Special cases aren't special enough to break the rules.

    Although practicality beats purity.
    
    Errors should never pass silently.
    
    Unless explicitly silenced.
    
    In the face of ambiguity, refuse the temptation to guess.
    
    There should be one-- and preferably only one --obvious way to do it.

    Although that way may not be
