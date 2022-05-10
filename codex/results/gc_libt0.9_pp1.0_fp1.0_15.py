import gc, weakref
import wx, wx.lib.sized_controls as sc
import wx.lib.buttons as buttons
import wx.lib.newevent

import pubsub

import config, controls
from bin.constants import logger

##------------------------------------------------------------------------

NodeSelectEvent, EVT_NODE_SELECT = wx.lib.newevent.NewEvent()
NodeEnterEvent, EVT_NODE_ENTER = wx.lib.newevent.NewEvent()
NodeExitEvent, EVT_NODE_EXIT = wx.lib.newevent.NewEvent()



##------------------------------------------------------------------------

_cache = dict()

def factory(parent, application=None):
    "Safely creates the gui elements for the given page, keeping only one page per widget"
    if (parent, application) in _cache: return _cache[(parent, application)]
    page = PropertyPage(parent, application)
    _cache[(parent, application)] = page
    return page



##------------------------------------------------------------------------

class PropertyPage(sc.SizedPanel):
    """Page controlling the modification of a
