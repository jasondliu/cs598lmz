import weakref

from .event import Event

from . import types
from . import util
from . import vfs
from . import widgets
from . import widgetutil
from . import window

from .widgetutil import AttrDict

from . import _cocoa

from . import _cocoa_types

from . import _cocoa_util

from . import _cocoa_graphics as graphics

from . import _cocoa_graphics_types as graphics_types

from . import _cocoa_graphics_util as graphics_util

from . import _cocoa_graphics_widgets as graphics_widgets

from . import _cocoa_graphics_window as graphics_window


def _apply_cocoa_appearance(obj):
    if isinstance(obj, _cocoa_types.NSView):
        obj.setWantsBestResolutionOpenGLSurface_(True)
    elif isinstance(obj, _cocoa_types.NSWindow):
        obj.setTitleVisibility_(0)
