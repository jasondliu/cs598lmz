import weakref

from . import _core
from . import _util
from . import _widget
from . import _window

class _App(object):
    def __init__(self):
        self._window_list = []
        self._window_list_lock = threading.Lock()
        self._window_list_cond = threading.Condition(self._window_list_lock)
        self._window_list_cond.acquire()
        self._window_list_cond.wait()
        self._window_list_cond.release()

    def _add_window(self, window):
        self._window_list_lock.acquire()
        self._window_list.append(window)
        self._window_list_cond.notify()
        self._window_list_lock.release()

    def _remove_window(self, window):
        self._window_list_lock.acquire()
        self._window_list.remove(window)
        self._window_list_lock.release()

    def _get_window_list(self):
        self._window_
