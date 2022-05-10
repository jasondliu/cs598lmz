import gc, weakref
from pymol import __init__
from pymol import cmd
from pymol import cgo
from pymol import util

import pymol

# import pymol.cgo
import contextlib
import traceback

def _get_id(obj):
    try:
        return id(obj)
    except TypeError:
        # can't get id of weakproxy
        return -1

class Widget(object):
    '''
    A Widget is an object which can be manipulated on screen in some way.
    The widget object is a simple object, and all of the actual state is
    stored in a "widget_data" object.  This allows the widget object to be
    copied, and the copied widget will share the same widget_data object.
    This is useful for creating a widget that stays in place while the
    objects it is based on move around.

    The widget_data object can be retrieved with the get_data() method.
    Normally, the widget_data object is a simple cgo object, but this is not
    required.

    The widget_data object
