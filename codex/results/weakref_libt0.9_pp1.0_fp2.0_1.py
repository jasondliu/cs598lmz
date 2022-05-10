import weakref, re, sys
import hal
import gobject

try:
    import gtk
    import gtk.gdk
except ImportError:
    gtk = None
    gdk = None

try:
    import cairo
except ImportError:
    cairo = None

__all__ = ["CanvasFrame", "TrueCanvas", "Style", "register_canvas"]

registry = []

_CAPS_ = {
    "butt": cairo.LINE_CAP_BUTT,
    "round": cairo.LINE_CAP_ROUND,
    "square": cairo.LINE_CAP_SQUARE,
    "CHAIN": cairo.LINE_CAP_CHAIN,
}

_JOINS_ = {
    "miter": cairo.LINE_JOIN_MITER,
    "round": cairo.LINE_JOIN_ROUND,
    "bevel": cairo.LINE_JOIN_BEVEL,
}

class CanvasError(RuntimeError):
    pass

class CanvasItem(object):
    object_list
