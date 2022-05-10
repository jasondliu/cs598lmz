import gc, weakref

from . import _cffi_backend

__all__ = ['new_handle', 'get_handle', 'release_handle', 'from_handle']

def new_handle(x):
    return _cffi_backend.newp_handle(x)

def get_handle(handle):
    return _cffi_backend.get_handle(handle)

def release_handle(handle):
    return _cffi_backend.releasep_handle(handle)

def from_handle(handle):
    return _cffi_backend.from_handle(handle)

# ____________________________________________________________

class HandleCache(object):
    _all_handles = {}

    def __init__(self, handle):
        self.handle = handle
        self.weakreflist = []
        self.weakreflist.append(weakref.ref(self, self._remove_handle))
        self.__class__._all_handles[handle] = self

    def _remove_handle(self, wr):
        self.
