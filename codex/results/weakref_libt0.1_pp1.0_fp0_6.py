import weakref

from . import _core
from . import _util
from . import _widget
from . import _window

__all__ = ['Application']


class Application(_core.Application):
    """
    Application class.

    This class is used to create the application.
    """

    def __init__(self, title='', width=640, height=480, **kwargs):
        """
        Create an application.

        Args:
            title (str): The title of the application.
            width (int): The width of the application.
            height (int): The height of the application.
            **kwargs: The keyword arguments passed to the super class.
        """
        super().__init__(title, width, height, **kwargs)

        self._windows = []

    def run(self):
        """
        Run the application.

        This method will run the application.
        """
        self._run()

    def quit(self):
        """
        Quit the application.

        This method will quit the application.
        """
        self._quit()

    def create_
