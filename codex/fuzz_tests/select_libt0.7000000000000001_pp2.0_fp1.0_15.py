import select
import socket
import threading
import time

from . import boolean, structs
from . import config
from . import connection
from . import protocol


log = logging.getLogger(__name__)


class Server(object):
    def __init__(self, addr, port, db,
                 max_connections=1024, backlog=5,
                 max_idle=3600.0, max_life=0.0,
                 shutdown_timeout=5.0,
                 compression_level=6,
                 use_ssl=False, ssl_keyfile=None, ssl_certfile=None,
                 use_auth=False, auth_file=None,
                 use_pooling=False,
                 pool_min_size=2, pool_max_size=None,
                 pool_init_size=None, pool_idle_timeout=None,
                 pool_conn_ttl=None, pool_stale_timeout=None,
                 use_suspend=False,
                 suspend_min_threads=1, suspend_max_threads=None,

