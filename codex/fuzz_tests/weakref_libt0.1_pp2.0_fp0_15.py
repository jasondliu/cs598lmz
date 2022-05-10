import weakref

from . import _core
from . import _util
from . import _widget
from . import _window

__all__ = ['App']


class App(_core.Object):
    """
    The App class represents a single application.

    An application is a single instance of a program.  It is
    responsible for creating and managing windows.

    The App class is a singleton, so you can only create one
    instance of it.  You can access the singleton instance using
    the :func:`get_running_app` function.

    The App class is a subclass of :class:`~kivy.event.EventDispatcher`,
    so you can bind to events on it.  For example, you can bind to the
    :attr:`on_start` event to be notified when the application has
    started::

        def on_start(self):
            print('The application has started!')

        app = App.get_running_app()
        app.bind(on_start=on_start)

    """

    __events__ = ('on_start', 'on_
