import mmap
import sys
import os
import errno
import threading
import time
import math

from . import util
from . import acl
from . import config
from . import client
from . import printlock
from . import zk
from . import snap
from . import zfs

from .constants import *
from .util import *

def check_zfs_version(major, minor, micro):
    version = zfs.get_version()
    if version is None:
        return False
    if version[0] < major:
        return False
    elif version[0] > major:
        return True
    if version[1] < minor:
        return False
    elif version[1] > minor:
        return True
    if version[2] < micro:
        return False
    return True

def check_zfs_vdev_scrub(pool):
    pool_name = pool['name']
    cmd = ['zpool', 'get', '-H', '-o', 'value', 'vdev_scrub_rate', pool_name]

