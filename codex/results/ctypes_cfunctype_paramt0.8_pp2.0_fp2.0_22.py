import ctypes
FUNTYPE = ctypes.CFUNCTYPE(None)

import sys
_logger = logging.getLogger('pyglet')
DEBUG = lambda *args: None
# DEBUG = lambda *args: _logger.info(' '.join([str(x) for x in args]))

# --- Globals ---------------------------------------------------------------

_default_event_loop = None
_event_queue = []

_display_flip = True

_time = 0
_set_time = None
_set_time = time.time
del time

_keyboard = None

_locks = threading.local()
_locks.count = 0
_locks.owner = None

# --- Exceptions ------------------------------------------------------------

class EventException(Exception):
    pass

# --- Functions -------------------------------------------------------------

def _run():
    global _event_queue
    
    while _event_queue:
        # NOTE: we make a copy of the event queue, since the callbacks
        # may push more events onto the queue.  Copying the queue here
        # means any new events are processed on the next iteration.
        queue = _event_queue
