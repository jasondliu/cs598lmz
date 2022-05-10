import ctypes
# Test ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int, ctypes.c_int)
@functools.lru_cache(maxsize=None)
def CmpFunc(arg1, arg2):
    return arg1 > arg2
# Test ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int)
@functools.lru_cache(maxsize=None)
def HashFunc(arg1):
    return 0

# readonly.
OrderedDictType = collections.OrderedDict

class SortedDict(OrderedDictType):
    """
    This is a readonly OrderedDict.
    """
    def __init__(self, *args, **kwargs):
        """
        Constructor.
        """
        self._cmp = kwargs.pop('cmp', None)
        self._key = kwargs.pop('key', None)
        self._reverse = kwargs.pop('reverse', False)
        super().__init__(*args, **kwargs)

