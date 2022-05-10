import ctypes
# Test ctypes.CField
class User(ctypes.Structure):
    _fields_ = [("id",ctypes.c_long),("name",ctypes.c_wchar_p)]
user = User()
user.id = 5
user.name = "qiwsir"
print(user.id,user.name)
user_p = ctypes.pointer(user)
user_p.contents.id = 9
user_p.contents.name = "python"
print(user.id,user.name)
# print(list(user))
print(user[0],user[1])
print(user.as_buffer((ctypes.c_wchar * 20)(),0))

# Test ctypes.Array
from ctypes import byref,c_int
class TestArray(ctypes.Structure):
    _fields_ = [("a",ctypes.c_long),("b",ctypes.c_int*(5))]
c_intp = ctypes.POINTER(c_int)
test_array = TestArray()
test_array.a = 3


