import signal
signal.signal(signal.SIGINT,signal.SIG_DFL)

def set_trace():
    """
    Sets an interactive breakpoint for the Python debugger
    """
    from IPython.core.debugger import Pdb
    from IPython.core import ultratb
    import sys
    sys.excepthook = ultratb.FormattedTB(call_pdb=True,color_scheme='Linux')
    Pdb().set_trace(sys._getframe().f_back)

import numpy as np
from numpy import *

from PyQt4.QtCore import *
from PyQt4.QtGui import *
from PyQt4 import uic

import os
import errno
import parameters
import gui
import targets
import geomutil
import data
from edit import edit_data
from data import get_data
import dataset


########################################################################################
def new_strategy_popup(parent,current_strategy=None):
    """
    Pop up a modeless dialog with an input field to create a
