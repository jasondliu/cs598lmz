import weakref

from .config import ConfigString, ConfigPath

from .utils import normalize, iface_names
from .exceptions import (
    ConnectionError, NoCrossConnections, InterfaceError,
    OperationalError, InterfaceNotFoundError)

from . import utils
from .chat import Chat
from .queue import Queue
from . import siface
from . import win32gui

import serial
from serial.tools import list_ports

from . import arduino

from .drivers import get_drivers, get_drivers_list

from .arduino_desc import *

import pkg_resources

DEFAULT_NOTIFY_ICON = os.path.join(os.path.abspath(os.path.dirname(__file__)),
    'arduino.ico')

class TrayIcon(object):
    """
    Gtk implementation of tray icon
    """
    def __init__(self, path=None, on_exit=None):
        self.icon_path = path
        self.on_exit = on_exit

        builder = gtk
