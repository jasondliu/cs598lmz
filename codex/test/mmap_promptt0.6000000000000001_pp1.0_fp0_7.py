import mmap
# Test mmap.mmap(fd, length, access=ACCESS_READ)

def test_mmap_write_access(testfile):
    with open(testfile, 'w+') as f:
        f.write(b'abcde')
        f.flush()
        with mmap.mmap(f.fileno(), 5, access=mmap.ACCESS_WRITE) as m:
            # Verify that modifications are made visible
            m[0] = b'B'
            assert f.read() == b'Bbcde'
            m[1:3] = b'XYZ'
            assert f.read() == b'BXYZe'
            m[:] = b'12345'
            assert f.read() == b'12345'
            # Verify that modifications are written to disk
            f.seek(0)
            m[:] = b'abcde'
            f.close()
            with open(testfile, 'rb') as f:
                assert f.read() == b'abcde'


