import gc, weakref
from . import _ext
from . import _util

def _get_malloc_size(obj):
    if isinstance(obj, _ext.NDArrayBase):
        return obj.size
    return 0

class _MemHookHandle(object):
    """Internal memory hook handle."""
    def __init__(self, callback):
        self._callback = callback
        self._ref = weakref.ref(self, self._destroy_callback)

    def __del__(self):
        if self._ref() is not None:
            _ext.mxMemHookRemove(self._callback)

    def _destroy_callback(self, _):
        self._callback = None

def _mem_hook_callback(event_type, nbytes, size, handle):
    """Internal memory hook callback."""
    if event_type == 0:
        event_type_str = 'malloc'
    elif event_type == 1:
        event_type_str = 'realloc'
    else:
        event_type_str = 'free'
    print('MemoryH
