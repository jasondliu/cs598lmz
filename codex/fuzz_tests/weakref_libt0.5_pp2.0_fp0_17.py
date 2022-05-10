import weakref

from tkinter import *
from tkinter.ttk import *
from tkinter.font import Font
from tkinter.messagebox import *
from tkinter.filedialog import *

import tkinter.ttk as ttk
import tkinter.font as tkf

from .calendar import *
from .timedelta import *
from .tkscrollframe import *
from .tkdateentry import *
from .tktimedeltaentry import *

from . import tkcalendar
from . import tktimedelta

# --------------------------------------------------------------------
#
# --------------------------------------------------------------------

def _test():
    root = Tk()
    root.option_add('*tearOff', FALSE)

    m = PanedWindow(orient=HORIZONTAL)
    m.pack(fill=BOTH, expand=1)

    left = Label(m, text='left pane')
    m.add(left)

    m2 = PanedWindow(orient=VERTICAL)
    m.add(m2)

    top = Label(m
