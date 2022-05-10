import mmap
# Test mmap.mmap(-1, size) for size > 0x40000000
size = 2**30
try:
    m = mmap.mmap(-1, size)
except (OverflowError, ValueError):
    pass
else:
    # Test mmap.mmap(-1, size) for size > 0x40000000
    size = 2**31
    try:
        m = mmap.mmap(-1, size)
    except (OverflowError, ValueError):
        pass
    else:
        # Test mmap.mmap(-1, size) for size > 0x80000000
        size = 2**32
        try:
            m = mmap.mmap(-1, size)
        except (OverflowError, ValueError):
            pass
        else:
            # Test mmap.mmap(-1, size) for size > 0x100000000
            size = 2**33
            try:
                m = mmap.mmap(-1, size)
            except (OverflowError, ValueError, WindowsError):
                pass
