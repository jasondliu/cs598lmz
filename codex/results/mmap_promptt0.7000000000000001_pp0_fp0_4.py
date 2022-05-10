import mmap
# Test mmap.mmap() failure, then SystemError after read()
with open('/dev/null', 'wb') as fp:
    m = mmap.mmap(fp.fileno(), 0)
    try:
        m.read()
    except ValueError:
        pass
    # Verify that attempting to read() after a failed mmap raises
    # SystemError, not segfault.  http://bugs.python.org/issue15639
    with support.captured_output("stderr") as stderr:
        with self.assertRaises(SystemError):
            m.read()


class MmapTestCase(unittest.TestCase):

    def setUp(self):
        # Create a file to be mmap'ed.
        with open(support.TESTFN, 'wb') as f:
            f.write(b'\0' * mmap.PAGESIZE)

    def tearDown(self):
        support.unlink(support.TESTFN)

    def test_init(self):
        m = mmap.mmap(-1, 1)
       
