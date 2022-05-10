import weakref

from . import _core
from . import _util
from . import _widget
from . import _resource
from . import _style
from . import _layout

_style.load_default_style()

class Widget(object):
    """
    Base class for all widgets.
    """

    def __init__(self):
        self._handle = _core.uiNewWidget(self.__class__.__name__)
        self._on_destroy = None
        self._on_draw = None
        self._on_resize = None
        self._on_mouse_event = None
        self._on_mouse_crossed = None
        self._on_mouse_wheel = None
        self._on_key_event = None
        self._on_enabled_changed = None
        self._on_visible_changed = None
        self._on_mapped_changed = None
        self._on_position_changed = None

    def destroy(self):
        """
        Destroy the widget.
        """
        _core.uiFreeWidget(self._handle)

    def
