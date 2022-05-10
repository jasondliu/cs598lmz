import weakref

from . import config
from . import core
from . import events
from . import logging
from . import widgets as widgets


class WindowSystem(events.EventEmitter):

    def __init__(self,
                 title=None,
                 width=None,
                 height=None,
                 fullscreen=False,
                 vsync=True,
                 resizable=False,
                 config=None,
                 vbo=True,
                 display=None,
                 screen=None):
        super(WindowSystem, self).__init__()
        self.display = display
        self.screen = screen
        self.fullscreen = fullscreen
        self.title = title
        self.config = config
        self.vsync = vsync
        self.resizable = resizable
        self.use_vbo = vbo
        self.__width = width
        self.__height = height
        self._backend_object = None
        self.window = None
        self.w, self.h = (width, height)
        self._initialized = False
        self._event_handlers
