import gc, weakref, sys
import os, re, types, copy

from .. import utils
from .. import config
from .. import __version__
from .. import gfx
from .. import events
from .. import widgets
from .. import constants
from .. import exceptions
from .. import _text
from . import _cocos_menu, _widget_constants
from . import _cocos_instrumentation

# For backwards compatibility
from . import _cocos_popup

#===============================================================================
# Globals
#===============================================================================

#===============================================================================
# Helpers
#===============================================================================

#===============================================================================
# CocosNode
#===============================================================================
class CocosNode(object):
    """
    CocosNode is the root class of all visual elements in Cocos.
    It is a generic class that holds any visual element, and
    also defines the basic properties and behaviours of every
    visual element in Cocos.

    CocosNode has several useful features:
    - it can contain children, and can be parent of other CocosNodes
    - it can be scheduled to execute a function
   
