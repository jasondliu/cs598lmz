import gc, weakref
import os, os.path
import sys

import wx

from wx.lib.embeddedimage import PyEmbeddedImage

#----------------------------------------------------------------------

def get_icon(icon_name):
    return eval(icon_name)

def get_bitmap(icon_name):
    return eval(icon_name).GetBitmap()

#----------------------------------------------------------------------
# These are the base icons that are used for the toolbar and menus
#

add_icon = PyEmbeddedImage(
    "iVBORw0KGgoAAAANSUhEUgAAABAAAAAQCAYAAAAf8/9hAAAABmJLR0QA/wD/AP+gvaeT"
    "AAAACXBIWXMAAAsTAAALEwEAmpwYAAAAB3RJTUUH1QMVDSsXzk3qeAAAAB1pVFh0Q29t"
    "bWVudAAAAAAAQ3JlYXRlZCB3aXRoIEdJTVBkLmUHAAACTElEQVQ4
