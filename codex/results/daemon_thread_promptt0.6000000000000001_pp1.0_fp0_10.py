import threading
# Test threading daemon
import time
import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from lib.logger import logger
from lib.utils import get_pid
from lib.utils import get_config
from lib.utils import get_full_path
from lib.utils import get_disk_free_space
from lib.utils import get_disk_total_space
from lib.utils import get_disk_percent
from lib.utils import get_cpu_percent
from lib.utils import get_memory_percent
from lib.utils import get_swap_percent
from lib.utils import get_network_io
from lib.utils import get_network_bytes_sent
from lib.utils import get_network_bytes_recv

from lib.statsd_client import StatsdClient


class StatsdThread(threading.Thread):
    """Send statsd message thread"""

    def __init__(self, thread_name, interval, config):
        threading.Thread.__init__(self)
        self.thread_name =
