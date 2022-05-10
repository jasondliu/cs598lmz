import select
import time
import getpass
from threading import Lock
from zookeeper.handlers import KeeperState, EventType

logger = logging.getLogger(__name__)

class Watcher(object):

    def __init__(self, func, *args):
        self.func = func
        self.args = args

    def process(self, event):
        self.func(self.zk, event, *self.args)


class ZKClient(object):

    DEFAULT_ACL = [ZOO_READ_ACL_UNSAFE]
    NO_WATCH = Watcher(lambda zk, event: None)

    def __init__(self, hosts):
        self.hosts = hosts
        self.connected = False
        self.watcher = None
        self.connect()
        self.__pid = os.getpid()
        self.daemon = True
        self.ready_event = threading.Event()
        self.ready_event.clear()
        self.write_lock = Lock()
        self.start()

    def connect
