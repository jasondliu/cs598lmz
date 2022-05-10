import weakref

from . import _core
from . import _util
from . import _widget
from . import _window

__all__ = ['App']


class App(_core.Object):
    """
    The App class represents a single application.

    An application is a single instance of a program.  It can have multiple
    windows, but only one main window.  The main window is the window that is
    automatically shown when the application is run.  It is also the window
    that is used to automatically quit the application when it is closed.

    The App class is a singleton, so you can only have one App object at a
    time.  You can access the current App object using the :attr:`current`
    attribute.

    The App class is a subclass of :class:`~flexx.event.HasEvents`. It emits
    the following events:

    * ``init``: when the app is initialized.
    * ``exit``: when the app is about to exit.
    * ``interaction``: when the user interacts with the app.
    * ``paint``: when the app needs to be
