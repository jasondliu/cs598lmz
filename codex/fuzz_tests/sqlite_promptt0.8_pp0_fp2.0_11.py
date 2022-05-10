import ctypes
import ctypes.util
import threading
import sqlite3
# Test sqlite3.connect
sqlite3.connect("")

import sys

class X11WindowMapping(object):

    @classmethod
    def get_window_dict_for_display(cls, displayStr):
        """
        Returns a dictionary mapping window IDs to window names.
        Only top-level windows are returned.
        """
        display = X11WindowMapping.get_display(displayStr)
        screen = display.ScreenOfDisplay(display.DisplayOfScreen(0), 0)
        r = screen.root
        children = r.QueryTree()[1]
        result = {}
        for child in children:
            window_name = child.GetProperty(X11WindowMapping.get_atom(display, "WM_NAME"))
            if window_name is not None:
                result[child.id] = window_name
        display.CloseDisplay()
        return result

    @classmethod
    def get_display(cls, displayStr):
        try:
            return X11WindowMapping._display
        except AttributeError:
            display = ctypes.cdll.LoadLibrary
