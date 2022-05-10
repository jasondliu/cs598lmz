import ctypes
# Test ctypes.CField()

class CTest(ctypes.Structure):
    _fields_ = [
        ('item', ctypes.CField('char[64]')),
    ]

#
# Create a string that is too long to fit into "item".
# Then set it, and see what happens.
#
test = CTest()
test.item = "a" * 100

if test.item != "a" * 64:
    raise RuntimeError("test")
