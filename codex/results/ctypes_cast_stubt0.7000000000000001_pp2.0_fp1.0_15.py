import ctypes
ctypes.cast(ctypes.pointer(ctypes.c_int(0)), ctypes.py_object).value = None
import wx
import wx.lib.newevent
import wx.lib.agw.pycollapsiblepane as PCP
import wx.lib.mixins.listctrl as listmix
import wx.lib.scrolledpanel as scrolled
import wx.lib.sheet as sheet
import wx.html as html
import wx.adv
import datetime
import os
import pprint
import sqlite3
import re

# Import custom modules
from config import *
from database import *
from dialogs import *
from functions import *
from frames import *
from tasks import *

(UpdateEvent, EVT_UPDATE) = wx.lib.newevent.NewEvent()
(SetFocusEvent, EVT_SET_FOCUS) = wx.lib.newevent.NewEvent()

class MainFrame(wx.Frame):
    def __init__(self, parent, title, connection, cursor):
        self.parent = parent
        self.conn = connection
