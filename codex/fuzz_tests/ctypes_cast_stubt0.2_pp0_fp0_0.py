import ctypes
ctypes.cast(0, ctypes.py_object)

# imports for Python2
try:
    import Tkinter as tk
except ImportError:
    import tkinter as tk

try:
    import ttk
    py3 = False
except ImportError:
    import tkinter.ttk as ttk
    py3 = True

import tkinter.font as tkFont

import tkinter.messagebox as tkMessageBox

import tkinter.filedialog as tkFileDialog

import tkinter.simpledialog as tkSimpleDialog

import tkinter.scrolledtext as tkScrolledText

import tkinter.colorchooser as tkColorChooser

import tkinter.commondialog as tkCommonDialog

import tkinter.dialog as tkDialog

import tkinter.tix as tkTix

import tkinter.ttk as tkttk

#import tkinter.constants as tkconstants

#import tkinter.dnd as tk
