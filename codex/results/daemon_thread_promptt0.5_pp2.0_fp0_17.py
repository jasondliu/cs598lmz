import threading
# Test threading daemon
from time import sleep

from . import log
from . import remote
from . import util
from . import event
from . import config

from .config import Config
from .log import Log
from .remote import Remote
from .util import Util
from .event import Event

from .data import Data
from .data import DataException

class Daemon:
    """
    Monitor and control remote hosts.
    """

    def __init__(self):
        self.log = Log()
        self.util = Util()
        self.event = Event()
        self.config = Config()
        self.remote = Remote()
        self.data = Data()

        self.exit = False

        self.threads = []
        self.targets = []

        self.log.debug("Daemon initialized.")

    def start(self):
        self.log.debug("Daemon starting.")

        # Load configuration
        self.config.load()

        # Load targets
        self.load_targets()

        # Load data
        self.data.load()

        # Initialize
