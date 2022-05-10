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
    try:
        # Initialization
        stdscr = initscr()
        # Turn off echoing
        noecho()
        # Turn off line buffering
        cbreak()
        # Turn on keypad mode
        keypad(stdscr, 1)
        if has_colors():
            start_color()
            use_default_colors()
        # Call the user's function
        rc = func(stdscr, *args, **kwds)
    finally:
        # Termination
        if 'stdscr' in locals():
            # Turn off keypad mode
            keypad(
