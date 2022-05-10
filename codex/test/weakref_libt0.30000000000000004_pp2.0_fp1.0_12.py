import weakref

from . import _core
from . import _util
from . import _widgets

from . import _core

from . import _util

from . import _widgets

class _Gtk(object):
    """
    A class for holding GTK+ related attributes.
    """
    def __init__(self):
        self.main_loop = None
        self.main_loop_thread = None
        self.main_loop_thread_id = None
        self.main_loop_running = False
        self.main_loop_quit = False
        self.main_loop_quit_lock = threading.Lock()
        self.main_loop_quit_event = threading.Event()
        self.main_loop_quit_event.set()
        self.main_loop_quit_event_lock = threading.Lock()
        self.main_loop_quit_event_lock.acquire()
        self.main_loop_quit_event_lock.release()
