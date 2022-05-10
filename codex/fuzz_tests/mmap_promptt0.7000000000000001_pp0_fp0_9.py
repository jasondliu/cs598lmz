import mmap
# Test mmap.mmap(0, 1) behavior.
import os
test_support.find_unused_port()
if not hasattr(os, 'O_RDWR'):
    raise unittest.SkipTest, 'os.O_RDWR required for this test'
with open(test_support.TESTFN, 'w+b') as f:
    f.write('\x00')
    f.flush()
    fd = f.fileno()
    m = mmap.mmap(fd, 1)
    m[:] = '\x01'
    m.flush()
    m.close()
with open(test_support.TESTFN, 'rb') as f:
    d = f.read()
    if d != '\x01':
        raise unittest.TestFailed(
            'mmap.mmap(0, 1) wrote the wrong thing: ' + repr(d))


def test_bad_arguments():
    # Try some illegal arguments.
    with open(test_support.TESTFN, 'wb') as fp:
        fp
