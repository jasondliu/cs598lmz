import _struct

import pykd
from pykd import *
import windbg

class sb_t(object):

    def __init__(self, addr):
        self.ptr = addr

    def __str__(self):
        return str(self.ptr)

    def __repr__(self):
        return "<sb_t at 0x%x>" % (self.ptr)

    def sb_data(self):
        return ptrDWord(self.ptr).cast(g_typedVarCache.getTypedVar('sb_data_t'))

    def as_size(self):
        return int(self.sb_data().sb_size)

    def as_str(self):
        return loadUnicodeString(self.ptr)

    def sb_storage(self):
        return ptrDWord(self.ptr).cast(g_typedVarCache.getTypedVar('sb_storage_t'))

    def sb_end(self):
        if self.sb_allocator().sb_check(self) > 0:
            return int
