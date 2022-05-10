import ctypes
import ctypes.util
import threading
import sqlite3
# Test sqlite3.connect(':memory:')


import time

from ctypes import *

__all__ = [ 'libsbp', 'SBP_START', 'SBP_END', 'MsgSBP', 'MsgCallback'  ]

class MsgSBP(object):
    def __init__(self, ptr, msg_set_callback, msg_unset_callback):
        self.ptr = ptr
        self._msg_set_callback = msg_set_callback
        self._msg_unset_callback = msg_unset_callback

    def __del__(self):
        if self.ptr is not None:
            self._free_msg_from_ptr(self.ptr, self._msg_unset_callback)

    @staticmethod
    def _free_msg_from_ptr(ptr, msgunset):
        msgunset(ptr)
        libsbp.sbp_msg_free(ptr)

    @staticmethod
    def _from_ptr(ptr, msgset, msgunset):
        if ptr is None:
            return None

        return MsgSBP
