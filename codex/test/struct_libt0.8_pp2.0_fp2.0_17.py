import _struct
import _socket
import _select
import _fcntl


## Exceptions
class AlarmInterrupt(Exception):
    pass

class CursesError(Exception):
    pass

class CursesValueError(Exception):
    pass

class CursesKeyError(Exception):
    pass


## Functions
## Function that is typically invoked from an interpreter's main loop
def wrapper(func, *args, **kwds):
    """Initialization and termination calls for curses programs."""
