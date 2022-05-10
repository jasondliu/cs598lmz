import mmap
# Test mmap.mmap.__doc__

def test_mmap_mmap_doc():
    """
    mmap.mmap(fileno, length[, tagname[, access[, offset]]]) -> mmap object

    Create a memory-map to an existing file.  The file must be openable using
    Python's builtin open() function, and must be seekable.

    The tagname and  access  parameters  are  as for the GNU libc function
    mmap().
    """
    mmap.mmap(0, 1)
    try:
        mmap.mmap(0, 1, 'foo')
        mmap.mmap(0, 1, 'foo', 'bar')
        mmap.mmap(0, 1, 'foo', 'bar', 0)
    except TypeError:
        pass
    else:
        raise TestFailed, 'mmap.mmap() did not raise a TypeError'

# Test mmap.mmap.__new__.__doc__

def test_mmap_mmap_new_doc():
    """
    mmap.
