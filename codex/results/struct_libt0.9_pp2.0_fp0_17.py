import _struct
import struct
import subprocess
import time

from datetime import timedelta
from functools import partial
from functools import wraps
from jinja2 import Environment
from multiprocessing.dummy import Pool
from queue import Queue
from queue import Empty
from requests import HTTPError
from requests import Session
from requests import Timeout
from requests.exceptions import SSLError
from urllib3.connection import verify_mode
from urllib3.connectionpool import HTTPConnectionPool
from urllib3.connectionpool import HTTPSConnectionPool
from urllib3.util import Retry
from urllib3.util.retry import Retry
from urllib3 import Timeout as UrlTimeout
from urllib3.exceptions import ConnectTimeoutError
from urllib3.exceptions import ReadTimeoutError

from booksonic_token_auth import BooksonicTokenAuth
from loggers import debug_log, info_log, warn_log, error_log
from util import json_dumps, json_loads

OS_TYPE = platform.system()

if OS_
