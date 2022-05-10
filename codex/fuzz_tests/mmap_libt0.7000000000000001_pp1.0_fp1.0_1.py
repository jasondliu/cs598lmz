import mmap
import sys

# GLOBALS #####################################################################

# Maximum size of a single mmap() mapping
# (Windows will only allow mappings up to 2GB in size)
MAX_MAPPING_SIZE = 2**31

# EXTENSIONS ##################################################################

# Override the default behavior of memoryview.cast() to allow casting
# from a ctypes instance to a memoryview.
_orig_cast = memoryview.cast
def _fixed_cast(*args, **kwargs):
    try:
        return _orig_cast(*args, **kwargs)
    except TypeError as e:
        # If the exception is due to the fact that the buffer object is
        # a ctypes instance, try casting it first to a buffer.
        if 'has no buffer interface' in str(e):
            args = list(args)
            args[0] = buffer(args[0])
            return _orig_cast(*args, **kwargs)
        raise
memoryview.cast = _fixed_cast

# CLASSES #####################################################################

class MmapCloser(object):

