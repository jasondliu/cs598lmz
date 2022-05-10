import weakref

from . import _core
from . import _util
from . import _widget
from . import _window

class _MenuItem(_widget.Widget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._on_select = _util.Event()

    @property
    def on_select(self):
        """The event that is triggered when the menu item is selected."""
        return self._on_select

    def _set_enabled(self, value):
        self._impl.set_enabled(value)

    def _set_visible(self, value):
        self._impl.set_visible(value)

    def _set_label(self, value):
        self._impl.set_label(value)

    def _set_shortcut(self, value):
        self._impl.set_shortcut(value)

    def _set_checkable(self, value):
        self._impl.set_checkable(value)

    def _set_checked(self, value):
        self
