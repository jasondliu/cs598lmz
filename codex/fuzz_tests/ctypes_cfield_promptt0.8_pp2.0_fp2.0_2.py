import ctypes
# Test ctypes.CField instance
ctypes._CDataMeta.GetFieldType = None
class TestCF:
	_fields_ = [('f1', ctypes.c_long, 0), ('f2', ctypes.c_ubyte, 0)]
TestCF._pack_ = 1
class TestCF2:
	_fields_ = [('f1', ctypes.c_long), ('f2', ctypes.c_ubyte)]
TestCF2._pack_ = 1

class TestPointerInstance:
	_fields_ = [('p', TestCF2)]
# Test that 0-length bitfield gets repr()ed as int
assert repr(TestCF().f1) == '0'
# Test that bitfield with 0 length becomes plain int
assert TestCF().f1.__class__ is ctypes.c_long
assert TestCF2().f1.__class__ is ctypes.c_long
# Test that bitfield-using struct's instance can be a pointer
p = ctypes.pointer(TestPointerInstance())
assert p.contents.p.f1 == 0
assert p.contents.
