import selectors
import sqlite3
import logging
import argparse
import io
import asyncio
import time
from itertools import repeat
from functools import partial
from collections import namedtuple, deque

from . import logger, config, db
from .util import size_to_string
from . import exceptions
from .exceptions import DownloadCanceled
from . import aria2_rpc
from .aria2_rpc import Aria2Exception
from .aria2_rpc import ARIA2_OK, ARIA2_DOWNLOAD_PAUSED, ARIA2_DOWNLOAD_COMPLETE, ARIA2_DOWNLOAD_ERROR
from .aria2_rpc import BT_DOWNLOAD_ACTIVE, BT_DOWNLOAD_WAITING, BT_DOWNLOAD_PAUSED, BT_DOWNLOAD_COMPLETE, BT_DOWNLOAD_ABANDONED
from .aria2_rpc import BT_FETCHING_METADATA, BT_FETCHED_METADATA


# TODO
# 1. add progress bars
# 2. add torrents to queue
# 3
