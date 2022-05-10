import weakref
from queue import Queue, Empty
import time
import os
import re
from threading import Thread

from gi.repository import GObject, GLib
import pygame.mixer
from pygame.mixer import music
from pygame.mixer import pre_init as mixer_pre_init
from pygame.mixer import Sound

from . import _base
from . import _mixer
from . import _util
from . import _threading
from . import _event
from . import _constants
from . import _music


class Sound(_base.Sound):
    """
    Sound represents a single sound sample.

    Sounds can be loaded from files or from the built-in resources.
    """

    def __init__(self, file):
        self._initialized = False
        self._file = file
        self._pygame_sound = None
        self._pygame_channel = None
        self._pygame_queue = Queue()

        if self._file is not None:
            self._pygame_sound = pygame.mixer.Sound(self._file)


