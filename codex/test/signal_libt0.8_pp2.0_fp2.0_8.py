import signal
signal.signal(signal.SIGINT, signal.SIG_DFL)

from gi.repository import GLib

from .__version__ import __version__
from .__version__ import __url__
from .__version__ import __description__
from .__version__ import __author__
from .__version__ import __copyright__
from .__version__ import __license__

from .preferences import Preferences
from .ui import UI
from .statusicon import StatusIcon
from .proxy import Proxy
from .network import Network
from .notify import notify
from .process import Process
from .dbus import DBus
from .battery import Battery
from .wifiman import WifiMan
from .autoswitch import AutoSwitch
from .lock import Lock
from .proxy import *
from .app import *
from .utils import *


class Main(object):
    """
        Main class
    """
    def __init__(self):
        self._loop = GLib.MainLoop()
        self._proxy = Proxy(self)

