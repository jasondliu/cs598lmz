import gc, weakref
from .base import BaseObject, _t
from .node import Node
from .image import Image
from .gl import *
from . import util

class View(BaseObject):
    """View Class

    The View Class defines a drawable viewport.  Views are used to
    correctly scale images and to draw objects relative to a particular
    portion of the canvas.  For example, to draw a movie on the top half
    of the screen, you could create a View with the bottom set to 0.5.

    A View can have child views.  When a child view is drawn, it is
    drawn within the area of its parent.  A child view can have a child
    view of its own.  When a child view is drawn, its parent view is not
    drawn.

    The coordinate system of a View is [0,0] in the upper left and [1,1]
    in the lower right.  Views are drawn with their center at the center
    of their parent view, or at the center of the canvas if no parent
    exists.
    """
    _property_defaults = {"x": 0.5
