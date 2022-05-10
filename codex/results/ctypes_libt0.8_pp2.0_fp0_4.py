import ctypes
ctypes.windll.user32.SetProcessDPIAware()

# -----------------------------------------------------------------------------
# Imports
# -----------------------------------------------------------------------------

import os
import sys

import wx

from wx.lib.agw import supertooltip

import pkg_resources

from . import views
from . import config
from . import logging

# -----------------------------------------------------------------------------
# Globals
# -----------------------------------------------------------------------------

logger = logging.getLogger(__name__)

# -----------------------------------------------------------------------------
# Classes
# -----------------------------------------------------------------------------

class About(views.View):
    def __init__(self, parent):
        super(About, self).__init__(parent)

        self.Sizer = wx.BoxSizer(wx.VERTICAL)

        self.Sizer.Add(wx.StaticText(self, label="About"), 0,
                       wx.ALIGN_CENTER, 0)

        s = "Version: {0}\n"
        s += "Website: https://github.com/ronaldadrian/wx-led-board\n"
        s += "Twitter: https://twitter.com/sbas
