import ctypes
# Test ctypes.CField.__set__
#
# The input is an integer, which should be equal to the bitfield width.
# The test is for an exception on overflow, i.e. if the bitfield does not
# fit in the destination.  The test is also for an exception when an
# attempt is made to set a bitfield that is not stored in the destination.
class TestcFieldset(unittest.TestCase):
    def test_set0(self):
        # Build the bitfield
        class Test0(ctypes.LittleEndianStructure):
            _pack_ = 1
            _fields_ = [("foo", ctypes.c_ubyte, 8)]
        #
        # Test an exception for value > bitfield width
        #
        for value in (256, 0x100):
            with self.subTest(value=value):
                self.assertRaises(ValueError, Test0().__setattr__, "foo", value)
    def test_set1(self):
        # Build the bitfield
        class Test1(ctypes.LittleEndianStructure):
            _pack
