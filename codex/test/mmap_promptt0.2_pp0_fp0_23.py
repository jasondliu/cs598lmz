import mmap
# Test mmap.mmap
#
# This test is a bit different from the others.  It is not a
# self-contained test, but rather a test that is run as part of the
# test_mmap.py test.  This is because it is not possible to create
# anonymous mmap objects on Windows.  This test is run as part of the
# test_mmap.py test because it needs to be run in the same process as
# the test_mmap.py test.
#
# This test is run by the test_mmap.py test by calling the
# test_mmap_anonymous() function.

def test_mmap_anonymous():
    # This test is only run on Windows.  It is not run on other
    # platforms because it is not possible to create anonymous mmap
    # objects on other platforms.
    if sys.platform != "win32":
        return

    # Create an anonymous mmap object.
    m = mmap.mmap(-1, 1024)

    # Check that the mmap object is anonymous.
    assert m.name is None

    # Check that the mmap
