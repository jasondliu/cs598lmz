import weakref

from . import _base
from . import _compat
from . import _util
from . import _wrapper
from . import _xcb

__all__ = ['Display']

class Display(_base.Display):
    """Display connection to an X server.

    The display is automatically closed when the object is garbage collected.
    """

    def __init__(self, display=None):
        """Connect to an X server.

        The display parameter specifies the name of the display to connect to.
        If it is None, the value of the DISPLAY environment variable is used.
        """
        if display is None:
            display = os.environ.get('DISPLAY')
        if display is None:
            raise ValueError('no display specified')
        self.display = display
        self.conn = _xcb.xcb_connect(display, None)
        if self.conn.contents.has_error:
            raise _util.DisplayConnectionError(self.conn.contents.has_error)
