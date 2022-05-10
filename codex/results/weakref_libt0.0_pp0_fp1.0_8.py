import weakref

from . import _core
from . import _util
from . import _widget
from . import _window

__all__ = ['App']


class App(_core.Object):
    """
    The App class represents the application itself.
    """

    def __init__(self, *args, **kwargs):
        super(App, self).__init__(*args, **kwargs)
        self._windows = []

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

    def create_window(self, title=None, width=None, height=None,
                      left=None, top=None, resizable=None,
                      fullscreen=None, visible=None,
                      style=None, background_color=None,
                      min_size=None, max_size=None,
                      on_close=None, on_resize=None,
                      on_full
