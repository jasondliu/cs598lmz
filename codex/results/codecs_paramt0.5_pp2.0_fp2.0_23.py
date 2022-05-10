import codecs
codecs.register_error('strict', codecs.ignore_errors)

import sys
import re
import os
import time
import socket
import struct

# from http://code.activestate.com/recipes/534109/
class NoDaemonProcess(multiprocessing.Process):
    # make 'daemon' attribute always return False
    def _get_daemon(self):
        return False
    def _set_daemon(self, value):
        pass
    daemon = property(_get_daemon, _set_daemon)

# We sub-class multiprocessing.pool.Pool instead of multiprocessing.Pool
# because the latter is only a wrapper function, not a proper class.
class MyPool(multiprocessing.pool.Pool):
    Process = NoDaemonProcess

# multiprocessing.Pool.map can't handle generator input
# from http://code.activestate.com/recipes/577564-multiprocessingpool-map-for-generators/
def mp_map(func, items, n_proc=None):
    if n
