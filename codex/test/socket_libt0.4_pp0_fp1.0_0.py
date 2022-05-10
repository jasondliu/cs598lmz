import socket
import sys
import threading
import time
import traceback
from collections import deque
from queue import Queue
from typing import List, Optional, Tuple

import websocket

from . import __version__
from .constants import (
    BLOCK_TIME,
    DEFAULT_TIMEOUT,
    MAX_RETRIES,
    MAX_RETRY_DELAY,
    MIN_RETRY_DELAY,
    RETRY_MULTIPLIER,
)
