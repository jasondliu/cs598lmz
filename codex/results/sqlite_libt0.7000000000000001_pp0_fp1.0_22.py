import ctypes
import ctypes.util
import threading
import sqlite3
import time

# -----------------------------------------------------------------------------
# pylint: disable=C0103
lib = ctypes.cdll.LoadLibrary( ctypes.util.find_library('X11') )
# pylint: enable=C0103


# -----------------------------------------------------------------------------
class Xlib( object ):
    """
    The X11 API
    """

    # -------------------------------------------------------------------------
    def __init__(self):

        # ---------------------------------------------------------------------
        # Create the function prototypes for the X11 API.
        # http://tronche.com/gui/x/xlib/display/manipulating-the-display.html
        # ---------------------------------------------------------------------

        # ---------------------------------------------------------------------
        # Display *XOpenDisplay(char *display_name);
        # ---------------------------------------------------------------------
        self.XOpenDisplay = lib.XOpenDisplay
        self.XOpenDisplay.argtypes = [ctypes.c_char_p]
        self.XOpenDisplay.restype = ctypes.c_void_p

        # ---------------------------------------------------------------------
        # int XCloseDisplay(Display *display_ptr);
        # ---------------------------------------------------------------------
        self.XCloseDisplay =
