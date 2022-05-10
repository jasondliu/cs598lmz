import weakref

from . import _core
from . import _util
from . import _widget
from . import _window

__all__ = ['Application']


class Application(_core.Application):
    """
    Application class.

    This class is a wrapper around the native application class.
    """

    def __init__(self, name, title, version, author, copyright,
                 description, url, license, icon, splash,
                 window_class=_window.Window,
                 widget_class=_widget.Widget,
                 **kwargs):
        """
        Initialize the application.

        :param name: The name of the application.
        :param title: The title of the application.
        :param version: The version of the application.
        :param author: The author of the application.
        :param copyright: The copyright of the application.
        :param description: The description of the application.
        :param url: The URL of the application.
        :param license: The license of the application.
        :param icon: The icon of the application.
        :param splash: The splash screen of the
