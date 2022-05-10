import weakref

from . import app, utils
from .exceptions import *
from .log import logger
from .utils import call_later, run_in_thread


class Remote(object):
    """Remote object."""

    def __init__(self, id, obj, observer=None, name=None):
        self.id = id
        self.obj = obj
        self.observer = observer
        self.name = name
        self._gobj = None
        self._is_destroyed = False

    def __repr__(self):
        if self.observer is None:
            return "<Remote %s>" % (self.id,)
        else:
            return "<Remote %s:%s>" % (self.observer.name, self.id)

    @property
    def gobj(self):
        if self._gobj is None:
            self._gobj = gobject.GObject.new(RemoteGObject, remote=self)
        return self._gobj

    def destroy(self):
        """Destroy."""
        if self._is_destroyed:
