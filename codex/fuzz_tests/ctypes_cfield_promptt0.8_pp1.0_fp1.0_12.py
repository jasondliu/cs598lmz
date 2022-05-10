import ctypes
# Test ctypes.CField for the expected behavior.

libc = ctypes.CDLL(ctypes.util.find_library('c'))

#
# Test 1: no field
#
class A(ctypes.Structure):
    _fields_ = []
print(A())

#
# Test 2: one field, no size
#
class B(ctypes.Structure):
    _fields_ = [('f', None)]
print(B())

#
# Test 3: nested fields
#
class C(ctypes.Structure):
    _fields_ = [('f', A)]
print(C())

#
# Test 4: nested fields, nested deeper
#
class D(ctypes.Structure):
    _fields_ = [('f', C)]
print(D())

#
# Test 5: nested fields, nested deeper 2
#
class E(ctypes.Structure):
    _fields_ = [('f', A), ('g', D)]
print(E())

#
# Test 6: nested fields, nested deeper 3
#
class F(ctypes.
