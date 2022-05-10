import weakref

from . import _base
from . import _util

class _W_GtkWidget(_base._W_GtkWidget):
    def __init__(self, obj):
        _base._W_GtkWidget.__init__(self, obj)
        self._obj = obj
        self._obj.set_data("pygobject", self)
        self._obj.connect("destroy", self._destroy_cb)

    def _destroy_cb(self, obj):
        self._obj = None

    def _get_obj(self):
        return self._obj

class _W_GtkContainer(_W_GtkWidget):
    def __init__(self, obj):
        _W_GtkWidget.__init__(self, obj)
        self._obj = obj
        self._obj.set_data("pygobject", self)
        self._obj.connect("destroy", self._destroy_cb)

    def _destroy_cb(self, obj):
        self._obj = None

    def _get_obj(self):
        return self._obj

