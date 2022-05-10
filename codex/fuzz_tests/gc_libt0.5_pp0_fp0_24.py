import gc, weakref
import threading

from . import utils

class _TkObject(object):
    """
    Base class for all objects that use Tkinter.

    This class is not public.
    """

    def __init__(self, master):
        self._master = master
        self._master_ref = weakref.ref(master)
        self._root = master._root
        self._root_ref = weakref.ref(master._root)
        self._tk = master._tk
        self._tk_ref = weakref.ref(master._tk)
        self._tcl = master._tcl
        self._tcl_ref = weakref.ref(master._tcl)
        self._setup()

    def _setup(self):
        pass

    def _destroy(self):
        pass

    def _get_master(self):
        return self._master_ref()

    def _get_tk(self):
        return self._tk_ref()

    def _get_root(self):
        return self._root_ref()

    def _get_t
