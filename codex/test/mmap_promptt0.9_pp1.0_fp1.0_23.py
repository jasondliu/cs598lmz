import mmap
# Test mmap.mmap(-1, 1), the ending is beyond the end of the mapping
buf = mmap.mmap(-1, 1)   # if (LONG_MAX < SSIZE_MAX), it
                        # returns ValueError: mmap offset is greater
                        # than system maximum
buf.close()

buf = mmap.mmap(-1, 0)   # doesn't return an OverflowError, but
                        # ValueError: mmap length is negative
buf.close()

buf = mmap.mmap(-1, -1)  # doesn't return an OverflowError or a
                        # ValueError, but returns an invalid MMAP
                        # object
buf.close()

# Test mmap.mmap(<posix.times_result>, 1), the ending is beyond the end of the
# mapping
import posix, mmap
stat_buf = mmap.mmap(0, 1).fstat()
buf = mmap.mmap(stat_buf, 1)
buf.close()

# Test mmap.mmap(<posix.times_result>, 0), the ending is at the end
