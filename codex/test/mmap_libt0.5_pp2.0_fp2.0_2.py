import mmap
import os
import re
import subprocess
import sys
import time
import traceback

import requests

from . import (
    config,
    logger,
    process,
    util,
)

_LOGGER = logger.get_logger(__name__)

_CONFIG_FILE = '/etc/nginx/nginx.conf'

_START_TIMEOUT = 10
_START_RETRIES = 5

_MAX_RETRIES = 5
_RETRY_TIMEOUT = 1

_HUP_TIMEOUT = 10

_DUMP_TIMEOUT = 10

_MAX_PORTS = {
    'http': 65535,
    'https': 65535,
}


class NginxError(Exception):
    pass


class NginxConfigError(NginxError):
    pass


class NginxManager(object):

    def __init__(self):
        self.nginx_pid = None
