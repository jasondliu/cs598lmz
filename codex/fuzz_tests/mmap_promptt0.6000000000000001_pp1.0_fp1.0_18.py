import mmap
# Test mmap.mmap
from test import test_support
from test.test_mmap import DATA_FILE
from test.test_mmap import DATA_SIZE

# XXX(nnorwitz): this test is not portable b/w Win and Unix.
# Perhaps we should use a different file on win32.
# See test.test_mmap

class MmapTests(unittest.TestCase):

    def test_basic(self):
        file_size = 1024
        map_size = 1024
        fd = os.open(test_support.TESTFN, os.O_CREAT | os.O_RDWR)
        os.write(fd, "\0" * file_size)
        m = mmap.mmap(fd, map_size)
        m[0:10] = "1234567890"
        os.close(fd)
        self.assertEqual(m[0:10], "1234567890")
        m.close()

    def test_size0(self):
        # Issue #11472: mmap with size 0 should not raise an exception
        f
