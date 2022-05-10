import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    print("fun")
    return
 
# to create a set of enum values use the following syntax:
# (enum name, (enum values))
# in this case the enum is named 'enum1' and two enum values are created
# with the integer values 0 and 1
 
# the last two None values are required for the create_set_enum_type
# function
