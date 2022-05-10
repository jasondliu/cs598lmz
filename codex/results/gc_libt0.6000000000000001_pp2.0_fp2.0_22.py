import gc, weakref

from . import _xcb
from . import xproto
from . import randr

from . import _util
from . import _keysyms

from . import _render
from . import _shm
from . import _xfixes

from . import _xinerama

from ._xcb import XCB_GC_FOREGROUND, XCB_GC_BACKGROUND

from . import _xcb_xfixes
from . import _xcb_xinput

from . import _xcb_randr

from . import _xcb_xkb

from . import _xcb_ewmh

from . import _xcb_keysyms

from . import _xcb_event

from . import _xcb_cursor

class xcb_connection_t(ctypes.Structure):
    """Structure representing an XCB connection to an X server.
    """
    pass

class xcb_window_t(ctypes.c_uint32):
    """Structure representing a window.
    """
    def __str__(self):
        return
