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

if do_hotplug():
    import usb.hotplug

class USBError(Exception):
    pass

class device(object):
    def __init__(self):
        self._fd = -1

    def __del__(self):
        if self._fd != -1:
            self.deinitialize()

    def _open(self, idx, nb_interface=1, **kwargs):
        try:
            self._fd = os.open('/dev/sequoia_v%d_%d' % (idx, nb_interface), os.O_RDWR)
        except Exception as e:
            raise USBError('could not open sequoia interface: %s' %
