import socket
import sys
import threading
import time
import traceback
from collections import namedtuple
from datetime import datetime
from enum import Enum
from functools import wraps
from typing import Any, Callable, Dict, List, Optional, Tuple, Type, Union

import requests
from requests.adapters import HTTPAdapter
from requests.packages.urllib3.util.retry import Retry

from . import __version__
from .constants import (
    DEFAULT_CONNECTION_TIMEOUT,
    DEFAULT_CONNECT_RETRIES,
    DEFAULT_HTTP_TIMEOUT,
    DEFAULT_MAX_RETRIES,
    DEFAULT_RETRY_BACKOFF_FACTOR,
    DEFAULT_RETRY_WAIT_SECONDS,
    DEFAULT_SSL_VERIFY,
    DEFAULT_USER_AGENT,
    DEFAULT_WAIT_BETWEEN_RETRIES,
    HTTP_RETRIABLE_ERRORS,
    HTTP_RETRIABLE_STATUS_CODES,
    HTTP_SU
