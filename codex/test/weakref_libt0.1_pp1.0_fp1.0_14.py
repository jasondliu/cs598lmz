import weakref

from . import _core
from . import _util
from . import _widget
from . import _window

__all__ = ['Application']


class Application(_core.Application):
    """
    Application class.

    This class is a singleton.
    """

    def __new__(cls, *args, **kwargs):
        if not hasattr(cls, '_instance'):
            cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self, *args, **kwargs):
        if hasattr(self, '_initialized'):
            return
        super().__init__(*args, **kwargs)
        self._initialized = True

    def run(self):
        """
        Run the application.

        This method will block until the application is closed.
        """
        self._run()

    def quit(self):
        """
        Quit the application.
        """
        self._quit()

