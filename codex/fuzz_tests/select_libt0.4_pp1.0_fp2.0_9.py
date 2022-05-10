import select
import time
import sys
import os
import signal
import socket
import errno
import logging
import logging.handlers
import threading
import traceback
import Queue
import random
import subprocess
import re
import copy
import json
import pprint

import paramiko

from binascii import hexlify

from paramiko.py3compat import b, u, decodebytes

# setup logging
logger = logging.getLogger('paramiko.transport')

SSH_PORT = 22
DEFAULT_MAX_PROMPT_WAIT = 10
DEFAULT_PROMPT_TIMEOUT = 2
DEFAULT_PROMPT_WAIT = 2
DEFAULT_PROMPT_RETRIES = 5
DEFAULT_PROMPT_RETRY_WAIT = 2
DEFAULT_PROMPT_RETRY_BACKOFF = 2
DEFAULT_TIMEOUT = 10
DEFAULT_BUFFER_SIZE = 65536
DEFAULT_MAX_BUFFER_SIZE = 65536
DEFAULT_SOCKET_TIMEOUT = None

# used for the prompt regex
