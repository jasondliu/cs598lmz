import ctypes
# Test ctypes.CField

#
# Use ctypes to populate the fields using ctypes magic.
#
if sys.platform == "win32":
    dll = ctypes.CDLL("test.dll")
    SetField_Int_func = dll.SetField_Int
    GetField_Int_func = dll.GetField_Int
else:
    dll = ctypes.CDLL("./test.so")
    SetField_Int_func = dll.SetField_Int
    GetField_Int_func = dll.GetField_Int

SetField_Int_func.restype = ctypes.c_int
SetField_Int_func.argtypes = [ctypes.c_int, ctypes.c_int]

GetField_Int_func.restype = ctypes.c_int
GetField_Int_func.argtypes = [ctypes.c_int]

SetField_Int_func(1, 5)
print("SetField_Int(1, 5), GetField_Int(1) = {}".format(GetField_Int_func(1)))


