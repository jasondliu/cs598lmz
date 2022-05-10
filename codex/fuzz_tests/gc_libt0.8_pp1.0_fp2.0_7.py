import gc, weakref

module = sys.modules[__name__]

for name, value in vars(module).copy().items():
    if isinstance(value, type) and issubclass(value, ctypes.Structure):
        value.__module__ = 'ctypes'
        setattr(ctypes, name, value)
        delattr(module, name)

del name, value, module

def _cast_addrspace(addrspace, value):
    """
    >>> _cast_addrspace(0, 0xffffff8001b61000)
    0x1b61000L
    >>> _cast_addrspace(3, 0x1b61000)
    0xffffff8001b61000L
    """
    return {0: lambda x: x >> 12,
            3: lambda x: x << 12}[addrspace](value)

class struct_timeval(ctypes.Structure):
    '''struct timeval {
            time_t         tv_sec;        /* seconds */
            suseconds_t    tv_usec;       /* microseconds */
