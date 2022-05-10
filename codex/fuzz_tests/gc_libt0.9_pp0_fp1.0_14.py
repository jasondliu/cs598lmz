import gc, weakref
from types import MethodType

from _weakrefset import WeakSet

from . import lz4wrap
from .color import *
from .cmds import Cmds
from .common import *
from .vector import *


###############################################################################
# Font Setup
###############################################################################
from .font import Font
from .font import _recentFonts
from .font import _openTypeOrdering
from .font import _instances
from .font import _setInstallFolder
from .font import _setDefaultFont
from .font import _setDefaultWindow
from .font import _setDefaultShortcutKeys


from .drawingTools import *
_instances.add(weakref.ref(globals()))


###############################################################################
# Utilities
###############################################################################
def AddObserver(event, function, *args, **kwargs):
	"""
	Add an observer to the given *event*.
	
	When the event is triggered the `function` will be called.
	You can pass optional positional and keyword arguments that will be passed to the `function` on event.
	"""
