import mmap
import os
import random
import re
import sys
import time

from collections import defaultdict

from . import config
from . import util
from . import xlogging

_logger = xlogging.getLogger(__name__)

g_config_path = '/usr/sbin/aio/config/disk_config.json'
g_config_path_bak = '/usr/sbin/aio/config/disk_config.json.bak'

g_disk_config = None


def init_disk_config():
    global g_disk_config
    if g_disk_config is None:
        g_disk_config = DiskConfig()
    return g_disk_config


def get_disk_config():
    return init_disk_config()


def get_disk_config_path():
    return g_config_path


def get_disk_config_bak_path():
    return g_config_path_bak


def get_disk_config_json():
    return get_disk_config().get_config_
