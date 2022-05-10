import ctypes
# Test ctypes.CField
#
def get_CField_member():
    field = ctypes.CField("x", ctypes.c_int, 0)
    return field.name

get_CField_member()

# Test ctypes.CStruct
#
def get_CStruct_member():
    class Test(ctypes.CStruct):
        _fields_ = [("x", ctypes.c_int),
                    ("y", ctypes.c_char * 5),
                    ("z", ctypes.c_int)]

    return Test.y.name

get_CStruct_member()
"#),
        Err("CStructFieldIndex")
    );
}
