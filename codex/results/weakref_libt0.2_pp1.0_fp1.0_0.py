import weakref

from . import _core
from . import _util
from . import _widget
from . import _window

__all__ = ['App']


class App(_core.Object):
    """
    The App class represents a single application.

    The App class is a singleton, so you should never create an instance of it.
    Instead, you should use the :func:`~App.get_running_app` function to get
    the current running instance.

    The App class is the base class for all applications. It provides the
    following features:

    * :class:`~kivy.core.window.Window` management.
    * :class:`~kivy.core.clipboard.Clipboard` management.
    * :class:`~kivy.core.text.LabelBase` management.
    * :class:`~kivy.core.image.Image` loading.
    * :class:`~kivy.core.audio.SoundLoader` loading.
    * :class:`~kivy.core.camera.Camera` management.
   
