import ctypes
import ctypes.util
import threading
import sqlite3
import os

from PyQt5.QtCore import QObject, QTimer, pyqtSignal, QThread

from . import util


class Plugin(QObject):
    """
    Base class for all plugins.
    """

    NAME = "Base class"
    DESCRIPTION = "Base class for all plugins."
    AUTHOR = "Mek"
    VERSION = "1.0"

    # TODO: This is just a test.
    # TODO: This should be a signal with a payload.
    # TODO: I should probably make a new class, or extend QThread.
    # TODO: This is a thread that does something.
    # TODO: I need to figure out how to use this class.
    # TODO: I think the idea is to extend this class, and call the start() method on it.
    # TODO: The start() method will then call the run() method.
    # TODO: The run() method is supposed to do something, and when it's done, emit the finished() signal.
    # TODO: Then it will be done.

