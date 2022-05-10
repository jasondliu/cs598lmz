import weakref
import re
import tkinter as tk

from tkinter import ttk, filedialog

from wx_widgets.wx_utils import *
from wx_widgets.wx_tabs import *
from wx_widgets.wx_tree import *
from wx_widgets.wx_viewer import *
from wx_widgets.wx_menus import *
from wx_widgets.wx_toolbar import *
from wx_widgets.wx_elements import *
from wx_widgets.wx_popups import *

from core.core import *
from core.core_sys import *
from core.core_utils import *

from core.core_data import *
from core.core_ui import *

#----------------------------------------------------------------------------------------------------------------------*

class plugin_wx (plugin_core, wx.Frame) :
  def __init__ (self, in_settings, in_core) :
    plugin_core.__init__ (self, in_settings, in_core)
    wx.Frame.__init__ (self
