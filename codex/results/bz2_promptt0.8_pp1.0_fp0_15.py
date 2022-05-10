import bz2
# Test BZ2Decompressor
try:
    # Test readline()
    f = bz2.BZ2File("/dev/null")
    f.readline()
except StopIteration:
    f.close()

# Test gzip.open()
try:
    import gzip
    # Test readline()
    f = gzip.open("/dev/null", "rb")
    f.readline()
    f.close()
except StopIteration:
    f.close()

try:
    import mmap
    # Test mmap(os.devnull, mmap.PAGESIZE, 'r')
    f = mmap.mmap(os.open('/dev/null', 0), mmap.PAGESIZE, 'r')
    f.readline()
    f.close()
except OSError:
    pass

# Test find_library
if hasattr(ctypes, 'find_library'):
    ctypes.find_library('c')

# Test weakref.KeyedRef
class Dummy:
    pass

d = Dummy()

