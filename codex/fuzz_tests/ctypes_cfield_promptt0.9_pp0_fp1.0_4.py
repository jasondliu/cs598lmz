import ctypes
# Test ctypes.CField
assert repr(CField(None, None)) == "<CField 'name': type>"
assert repr(CField(None, None, None)) == "<CField 'name': type>" # XXX
assert repr(CField(None, None, None, None)) == "<CField 'name': type>" # XXX
# Test ctypes.CLibrary
assert repr(CLibrary("name", None)) == "<CLibrary 'name': None>"
assert repr(CLibrary("name", None, None, None)) == "<CLibrary 'name': None>" # XXX
assert repr(CLibrary("name", None, None)) == "<CLibrary 'name': None>" # XXX

class CStructureUnionTestCase(unittest.TestCase):
    FUNCTIONS = [("square", [("a", ctypes.c_int), ("b", c_int_p)]),
                 ("square2", [("a", ctypes.c_int), ("b", c_int_p)]) ]

    def __init__(self, val):
        super(CStructureUnionTestCase, self).__init__(val)
       
