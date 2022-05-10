import weakref

from . import _core
from . import _util
from . import _widget
from . import _window

__all__ = ['Application']


class Application(_core.Application):
    """
    The application object.

    This is the main object that manages the application.
    """

    def __init__(self, name, title=None, icon=None,
                 width=None, height=None, left=None, top=None,
                 resizable=True, style=None, full_screen=False,
                 visible=True, config_dir=None, config_file=None,
                 config_use_global=True, config_save_on_exit=True,
                 config_encoding='utf-8', config_auto_load=True,
                 config_auto_save=True, use_default_theme=True,
                 **kwargs):
        """
        Create an application object.

        :param name: The name of the application.
        :param title: The title of the application.
        :param icon: The icon of the application.
        :param width: The
