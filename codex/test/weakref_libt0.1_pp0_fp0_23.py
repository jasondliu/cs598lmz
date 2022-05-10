import weakref

from . import _core
from . import _util
from . import _widget
from . import _window

class _App(object):
    def __init__(self):
        self._window_list = []
        self._window_map = {}
        self._window_id_map = {}
        self._window_id_counter = 0
        self._window_id_map_lock = threading.Lock()
        self._window_map_lock = threading.Lock()
        self._window_list_lock = threading.Lock()
        self._window_id_map_lock.acquire()
        self._window_map_lock.acquire()
        self._window_list_lock.acquire()
        self._window_id_map[0] = None
        self._window_id_counter = 1
        self._window_id_map_lock.release()
        self._window_map_lock.release()
        self._window_list_lock.release()
        self._window_id_map_lock.acquire()
        self._window_map
