import weakref

from . import _core
from . import _util
from . import _widget
from . import _window

__all__ = ['Application']


class Application(_core.Application):
    """
    Application class.

    This class is a singleton.
    """

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._windows = weakref.WeakSet()

    def _add_window(self, window):
        self._windows.add(window)

    def _remove_window(self, window):
        self._windows.discard(window)

    def _get_windows(self):
        return list(self._windows)

    def _get_window_count(self):
        return len(self._windows)

    def _get_active_window(self):
        for window in self._windows:
            if window.is_active:
                return window

    def _set_active_window(self, window):
        if window is not None:
            window.activate()

    def
