import weakref

from .common import *
from . import common
from . import _cocos
from . import actions
from . import director
from . import event_dispatcher
from . import layer
from . import menu
from . import scene
from . import sprite
from . import scheduler
from . import touch_handler
from . import transition
from . import base_classes
from . import deprecated
from . import draw
from . import config

#
# pyglet related imports
#
import pyglet
from pyglet.gl import *

#
# cocosnode
#
class CocosNode(pyglet.event.EventDispatcher):
    """Base class for anything that gets drawn or contains things that get drawn.

    This is an abstract class. You should not create an instance of this class
    directly.

    All of the node attributes are lists. They are either empty or have one
    element for each child node.
    """
    x = 0
    y = 0
    rotation = 0
    scale = 1
