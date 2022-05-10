import mmap
# Test mmap.mmap.resize() method, kernel pagesize handling.



# This will cause random failures - the resize test is very racy.  Skip it.
@unittest.skip("The resize() method is very racy and causes intermittent "
               "failures")
class MMapTestCase(unittest.TestCase):

    def setUp(self):
        unittest.TestCase.setUp(self)
        self.fname = test.support.TESTFN

    def tearDown(self):
        unittest.TestCase.tearDown(self)
        test.support.unlink(self.fname)

    def test_resize_mmap(self):
        # Test that mmap.resize() returns a new offset into the resized file
        # and doesn't attempt to copy the contents from the original mmap.
        f = open(self.fname, "w+b")
        f.write(b"0")
        f.flush()
        f.seek(0)
        m = mmap.mmap(f.fileno(), 0)
       
