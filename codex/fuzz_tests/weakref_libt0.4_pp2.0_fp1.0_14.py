import weakref

from PyQt5.QtCore import QObject
from PyQt5.QtCore import pyqtSignal

from . import core
from . import utils


class Signal(QObject):
    """
    A Signal is a wrapper around a pyqtSignal that allows for
    the following:

    - A Signal can be called without arguments, and the Signal
      will emit itself.
    - A Signal can be called with a single argument, and the
      Signal will emit that argument.
    - A Signal can be called with multiple arguments, and the
      Signal will emit a tuple of those arguments.

    """
    def __init__(self, *args, **kwargs):
        super().__init__()
        self.signal = pyqtSignal(*args, **kwargs)

    def __call__(self, *args):
        if len(args) == 0:
            self.signal.emit(self)
        elif len(args) == 1:
            self.signal.emit(args[0])
        else:
            self.signal
