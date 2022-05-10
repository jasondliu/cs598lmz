import gc, weakref
import pdb
import atexit

from . import Base, PYTHON3, PYTHON2, CAN_CHANGE_IMAGE, CAN_SELECT_FROM_PANEL, CAN_ATTACH_WIDGET, \
                 NEW_ID_COUNTER, DIRTY_PICTURES, SAFE_MODE, USE_MCTL, is_debug, \
                 CAN_SEND_MODIFIED, CAN_SEND_NEW_IMAGE, GET_THUMBNAIL, GET_THUMBNAIL_SCALE, \
                 GET_THUMBNAIL_OFFSET, GET_THUMBNAIL_ROTATION
import wx
from wx import artprovider_v2 as artprovider
from wx.lib.art import NativeArt, SpottedArtProvider, CraftArtProvider, StockartArtProvider, \
                         LibartArtProvider, DC(DCNativeArtProvider)
from wx.lib.embeddedimage import PyEmbeddedImage

import wx.lib.filebrowsebutton as filebrowse
import wx.lib.throbber
