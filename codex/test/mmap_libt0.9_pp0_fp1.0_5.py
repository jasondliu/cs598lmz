import mmap
import fcntl
import select
import time
from os.path import dirname as up

from .. import util

from usb import hotplug_lib

def do_hotplug():
    return util.try_first(
        lambda: '/dev/sequoia_hotplug' in os.listdir('/dev'),
        lambda: False,
    )
