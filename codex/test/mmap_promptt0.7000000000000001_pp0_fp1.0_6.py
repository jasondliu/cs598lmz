import mmap
# Test mmap.mmap.  Use a function to avoid leaving a file lying around.
def test_mmap():
    f = open(test.support.TESTFN, "w+b")
