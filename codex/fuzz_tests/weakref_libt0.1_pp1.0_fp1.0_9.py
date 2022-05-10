import weakref

from . import _core
from . import _util
from . import _widget
from . import _window

class _MenuItem(_core.Object):
    def __init__(self, label, shortcut, callback, *args, **kwargs):
        super(_MenuItem, self).__init__(*args, **kwargs)
        self._label = label
        self._shortcut = shortcut
        self._callback = callback
        self._args = args
        self._kwargs = kwargs
        self._submenu = None
        self._checkable = False
        self._checked = False
        self._enabled = True
        self._visible = True
        self._radio = False
        self._radio_group = None
        self._radio_group_id = None
        self._radio_group_value = None
        self._radio_group_callback = None
        self._radio_group_args = None
        self._radio_group_kwargs = None
        self._radio_group_exclusive = False
        self._radio_group_exclusive_value = None
        self._radio_
