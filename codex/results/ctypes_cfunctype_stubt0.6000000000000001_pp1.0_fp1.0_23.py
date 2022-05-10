import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    return "hello"

fun.__name__ = "fun"

import warnings
with warnings.catch_warnings():
    warnings.simplefilter("ignore", category=DeprecationWarning)
    import tkinter
    import tkinter.ttk
    import tkinter.constants
    import tkinter.dialog
    import tkinter.simpledialog
    import tkinter.messagebox
    import tkinter.scrolledtext
    import tkinter.colorchooser
    import tkinter.filedialog
    import tkinter.commondialog
    import tkinter.font
    import tkinter.ttk

from . import config
from . import keybinding
from . import log
from . import tkutil
from . import util
from . import widget
from . import command
from . import configDialog
from . import editDialog
from . import color
from . import dialog
from . import findDialog
from . import gotoDialog
from . import help
from . import idleConf
from . import macosxSupport
from . import rpc
