import select
# Test select.select() for bad FDs
import _testcapi

# The value of RLIMIT_NOFILE is not necessarily the actual maximum
# FD limit.  On Linux, the limit is set to a value of at least 1024 by
# default, but getrlimit() would yield the actual limit.
_, hard = resource.getrlimit(resource.RLIMIT_NOFILE)

# Make sure that the getrlimit patch on OS X is working.
if sys.platform == 'darwin':
    try:
        import ctypes
    except ImportError:
        raise unittest.SkipTest("ctypes not supported")
    try:
        libc_name = ctypes.util.find_library('c')
        libc = ctypes.CDLL(libc_name, use_errno=True)
        getrlimit = libc.getrlimit
    except OSError as e:
        raise unittest.SkipTest("%s" % (e,))

    class rlimit(ctypes.Structure):
        _fields_ = [("rlim_cur", ctypes.
