import ctypes
import ctypes.util
import threading
import sqlite3
import time

# Import the python-xlib module
try:
    import Xlib
except ImportError:
    raise ImportError("Unable to find the python-xlib module. "
                      "Please install it and try again.")

# Import the python-xlib.xobject.drawable module
try:
    from Xlib.xobject.drawable import Window, Pixmap
except ImportError:
    raise ImportError("Unable to find the python-xlib.xobject.drawable "
                      "module. Please install it and try again.")

# Import the python-xlib.xobject.colormap module
try:
    from Xlib.xobject.colormap import Colormap
except ImportError:
    raise ImportError("Unable to find the python-xlib.xobject.colormap "
                      "module. Please install it and try again.")


class XScreenSaverInfo(ctypes.Structure):
    """Ctypes structure for the XScreenSaverInfo struct.
    """

