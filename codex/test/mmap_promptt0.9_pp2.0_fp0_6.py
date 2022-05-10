import mmap
# Test mmap.mmap(-1, ...) by creating a file and duplicating a file descriptor
# to a negative value.
# NOTE: This test will fail if the OS doesn't support duplicating a file
# descriptor to a negative value.
def test_mmap_negative_fd():
    # Create a file.
    fd = os.open('mmapfile', os.O_CREAT | os.O_RDWR, 0o777)
    os.write(fd, b'1234')
    os.close(fd)
    # Verify that mmap has documentation.
    assert mmap.__doc__
    # Verify that mmap opens a file and that the mapping starts at zero.
    with mmap.mmap(4) as m:
        m.seek(0)
        data = m.read(4)
        assert data == b'1234'
        # Verify that offset has the right value.
        assert m.offset == 0
    # Duplicate the file descriptor.
    newfd = -8
    os.dup2(fd, newfd)
    # Verify that we can open the file
