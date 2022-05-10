import weakref

from . import _core
from . import _util
from . import _widget
from . import _window

class _WindowImpl(_window.Window):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._impl = None
        self._created = False

    def _ensure_created(self):
        if self._created:
            return
        self._impl = self._create_window_impl(self)
        self._created = True

    def _create_window_impl(self, window):
        raise NotImplementedError()

    def _destroy_window_impl(self):
        raise NotImplementedError()

    def _set_title_impl(self, title):
        raise NotImplementedError()

    def _set_position_impl(self, position):
        raise NotImplementedError()

    def _set_size_impl(self, size):
        raise NotImplementedError()

    def _set_minimum_size_impl(self, size):
       
