import weakref

from . import _core
from . import _util
from . import _widget
from . import _window

class _App(_core.Object):
    def __init__(self, app):
        super().__init__()
        self._app = app
        self._app.set_object_self(self)
        self._app.set_object_id(self.get_id())
        self._app.set_object_destroy_func(self._destroy_func)
        self._app.set_object_on_destroy_func(self._on_destroy_func)
        self._app.set_object_on_event_func(self._on_event_func)
        self._app.set_object_on_update_func(self._on_update_func)
        self._app.set_object_on_paint_func(self._on_paint_func)
        self._app.set_object_on_key_down_func(self._on_key_down_func)
        self._app.set_object_on_key_up_
