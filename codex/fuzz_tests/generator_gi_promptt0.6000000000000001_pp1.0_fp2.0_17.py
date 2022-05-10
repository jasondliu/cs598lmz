gi = (i for i in ())
# Test gi.gi_code.co_flags for the existence of CO_ITERABLE_COROUTINE
# (see https://github.com/python/cpython/blob/3.9/Include/code.h).
if gi.gi_code.co_flags & 0x00000100:
    del gi
    __all__.append('async_generator')
