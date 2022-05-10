import mmap
# Test mmap.mmap(-1,1,access=mmap.ACCESS_WRITE)
#
# This test is for issue #14572, where a crash occurred when mmap() was
# called with an invalid file descriptor.
#

try:
    m = mmap.mmap(-1, 1, access=mmap.ACCESS_WRITE)
except ValueError:
    print("ValueError")
except OSError:
    print("OSError")
except mmap.error:
    # On some Python versions, mmap.error is raised on Windows.
    print("mmap.error")
except:
    print("Unexpected error:", sys.exc_info()[0])
    raise
else:
    print("Success")
