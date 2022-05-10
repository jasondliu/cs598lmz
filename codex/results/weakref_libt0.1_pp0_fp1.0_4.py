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

    def __init__(self, *args, **kwargs):
        """
        Create an application.

        :param args:
            Arguments to pass to the :class:`~urwid.MainLoop` constructor.
        :param kwargs:
            Keyword arguments to pass to the :class:`~urwid.MainLoop`
            constructor.
        """
        super().__init__(*args, **kwargs)
        self._windows = weakref.WeakValueDictionary()

    def run(self):
        """
        Run the application.

        This method will create a :class:`~urwid.MainLoop` and run it.
        """
        self.loop = _util.MainLoop(self.widget, self.palette, self.unhandled_input,
                                   self.screen
