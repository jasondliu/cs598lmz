import mmap
# Test mmap.mmap(0,1) == '\x00'
# Test mmap.mmap(0,2) == '\x00\x00'
# Test mmap.mmap(0,3) == '\x00\x00\x00'
# Test mmap.mmap(0,4) == '\x00\x00\x00\x00'
# Test mmap.mmap(0,5) == '\x00\x00\x00\x00\x00'
def get_size(size):
    if size == 0:
        return '\x00'
    return get_size(size - 1) + '\x00'

def test_mmap_signature(size):
    """
    >>> test_mmap_signature(1)
    '\x00'
    >>> test_mmap_signature(2)
    '\x00\x00'
    >>> test_mmap_signature(3)
    '\x00\x00\x00'
    >>> test_mmap_signature(4)
