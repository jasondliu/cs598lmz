import mmap
# Test mmap.mmap(0, 1, access=mmap.ACCESS_READ) with read-only access on a
# zero-length mapping.

with mmap.mmap(0, 0, access=mmap.ACCESS_READ) as m:
    try:
        m[0] = b'a'
    except ValueError:
        pass
    else:
        raise RuntimeError('mmap.ACCESS_READ on a zero-length mapping should '
                           'raise ValueError.')
