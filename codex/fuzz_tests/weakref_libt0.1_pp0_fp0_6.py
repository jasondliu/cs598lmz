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
        """
        Create a new App object.
        """
        super(App, self).__init__(*args, **kwargs)
        self._windows = []

    def run(self):
        """
        Run the application.
        """
        _core.lib.glfwInit()
        try:
            self._run()
        finally:
            _core.lib.glfwTerminate()

    def _run(self):
        """
        Run the application.
        """
        while True:
            _core.lib.glfwPollEvents()
            if not self._windows:
                break
            for window in self._windows:
                if window.should_close:
                    window.close()
                else:
                    window.draw()
