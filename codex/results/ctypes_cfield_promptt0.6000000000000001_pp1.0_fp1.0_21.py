import ctypes
# Test ctypes.CField
class CTest(ctypes.Structure):
    _fields_ = [
        ("field1", ctypes.c_int),
        ("field2", ctypes.c_int),
        ("field3", ctypes.c_int),
    ]

print(CTest)
ct = CTest()
print(ct.field1)
print(ct.field2)
print(ct.field3)

ct.field1 = 1
ct.field2 = 2
ct.field3 = 3
print(ct.field1)
print(ct.field2)
print(ct.field3)

# Test ctypes.CField.from_address
# create CTest type
CTest_p = ctypes.POINTER(CTest)
# create CTest instance at address 0x12345678
ct_p = ctypes.cast(0x12345678, CTest_p)
# initialize CTest instance
ct_p.contents.field1 = 1
ct_p.contents.field2 = 2
ct_p.contents.field3 = 3
print(
