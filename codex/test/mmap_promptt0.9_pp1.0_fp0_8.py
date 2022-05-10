import mmap
# Test mmap.mmap's size limit. On UNIX, it can be any size, but Windows
# has an upper limit of about 4 GB for 32-bit Python. Note that this test
# is inherently non-portable, since the underlying OS will have various
# limits on the overall resources available to a single process and the
# upper limit may be as low as 1 GB or less.

filename = TESTFN
SIZE = 10 * mmap.PAGESIZE

with open(filename, 'w+b') as f:
    # Extend the file to the desired size.
    f.truncate(SIZE)

    # On Windows, %loadfile truncates the file.
    m = mmap.mmap(f.fileno(), SIZE, access=mmap.ACCESS_WRITE)
    assert m.tell() == 0, 'mmap.mmap did not set file position to zero'

    if is_py3:
        # U+03C0 is the Unicode code point for the lowercase pi symbol.
        m.write(b'\xce\x80')
    elif is_jython:
        m
