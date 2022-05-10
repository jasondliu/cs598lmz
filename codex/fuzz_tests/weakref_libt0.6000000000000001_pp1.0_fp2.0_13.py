import weakref
import threading
import time

__all__ = ["get_hub", "get_default_hub", "Hub", "Thread", "reactor",
           "_threadlocal", "use_hub", "is_event_loop_running"]

_threadlocal = threading.local()

def get_hub():
    """Return the currently running event loop, or None if there is none.

    The event loop is thread-local.
    """
    try:
        return _threadlocal.hub
    except AttributeError:
        return None

def get_default_hub():
    """Return the default event loop.

    If this is called from a thread that has an active event loop,
    then that event loop is returned.  Otherwise, the default
    event loop is returned.

    The default event loop is determined by first checking
    whether the current thread has an active event loop, and if
    not, whether the main thread has an active event loop.  If
    both threads have inactive event loops, then a new event
    loop is created and set as the main event loop.
    """
    hub =
