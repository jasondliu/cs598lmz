import weakref

from . import _core
from . import _util
from . import _widget
from . import _window

class _App(_core.Object):
    """
    The application object.

    This object is automatically created by the first call to
    :func:`~kivy.app.App.run`.

    .. versionadded:: 1.0.7

    .. versionchanged:: 1.8.0

        The `App` class is now a subclass of :class:`~kivy.core.object.Object`.
    """

    __events__ = ('on_start', 'on_stop', 'on_pause', 'on_resume',
                  'on_config_change', 'on_low_memory', 'on_window_focus',
                  'on_window_blur', 'on_request_close', 'on_request_hide',
                  'on_request_show', 'on_request_update', 'on_has_window',
                  'on_new_window', 'on_window_remove')

    def __init__(self, **kwargs):
        self._
