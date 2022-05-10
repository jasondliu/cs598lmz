import weakref

from . import _core
from . import _util
from . import _widgets
from . import _windows

__all__ = ['Application']


class Application(_core.Application):
    """
    The main application class.

    This class is the main entry point for the application. It is responsible
    for creating the main window, and for handling the main event loop.

    The application object is a singleton, and can be accessed via the
    :py:func:`get_application` function.

    :param str name: The name of the application.
    :param str version: The version of the application.
    :param str description: A description of the application.
    :param str author: The author of the application.
    :param str copyright: The copyright of the application.
    :param str license: The license of the application.
    :param str url: The URL of the application.
    :param str icon: The icon of the application.
    :param str splash: The splash screen of the application.
    :param str locale: The locale to use for the application.
    :param str theme
