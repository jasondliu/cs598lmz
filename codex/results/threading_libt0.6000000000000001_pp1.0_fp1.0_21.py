import threading
threading.currentThread().setName("Main")

from . import autosubliminal
from . import core
from . import library
from . import scheduler
from . import webserver
from .version import __version__
