import select
import sys
import time

from argparse import ArgumentParser
from collections import namedtuple
from hashlib import md5
from logging import getLogger
from typing import Any, Dict, List, Optional, Tuple

from psycopg2 import DatabaseError, InterfaceError, OperationalError, connect

from . import __version__
from . import config
from . import log
from . import utils
from . import watcher
from .config import Config

logger = getLogger(__name__)

# Type aliases
DictStrAny = Dict[str, Any]
ListStrAny = List[Any]

# Named tuple for a database connection.
DbConnection = namedtuple("DbConnection", "conn, cursor")

# Named tuple for a database connection pool.
DbPool = namedtuple("DbPool", "connections, size")

# Named tuple for a database connection pool.
DbInfo = namedtuple("DbInfo", "name, conn_pool")

# Named tuple for a database connection pool.
DbConfig = namedtuple("DbConfig", "host, port,
