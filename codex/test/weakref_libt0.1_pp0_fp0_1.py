import weakref

from . import _core
from . import _util
from . import _widget
from . import _window

__all__ = ['Application']


class Application(_core.Application):
    """
    The application object.

    This is the main object of the application. It is responsible for
    creating the main window and for running the application.
    """

