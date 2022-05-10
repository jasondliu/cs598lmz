import socket
import sys
import time
import threading
import traceback
import os
import errno
import signal
import re
import subprocess
import json
import hashlib
import base64
import random
import string
import shutil
import requests

from . import config
from . import utils
from . import constants
from . import log
from . import exceptions
from . import __version__

logger = log.get_logger(__name__)

def get_host_ip():
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(('8.8.8.8', 80))
        ip = s.getsockname()[0]
    finally:
        s.close()
    return ip

def get_host_name():
    return socket.gethostname()

def get_host_uuid():
    host_uuid_file = os.path.join(config.get_workspace(), ".host_uuid")
    if os.path.exists(host_uu
