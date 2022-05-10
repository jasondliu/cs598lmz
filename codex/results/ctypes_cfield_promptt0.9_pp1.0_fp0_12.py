import ctypes
# Test ctypes.CField's __get__ method
# by creating a structure and assigning values 
struct_9 = ctypes.Structure(
    "struct_9", 
    # struct field and name is int i
    # a CField that contains the offset into the data 
    # buffer where <int i> is located and
    # a <get> method that reads the integer at that location.
    ("i", ctypes.CField, "Get i value"), 
    # struct field and name is int j
    # a CField that contains the offset into the data 
    # buffer where <int j> is located and
    # a <get> method that reads the integer at that location.
    ("j", ctypes.CField, "Get j value")
)

# Create a struct instance
s = struct_9(i=1, j=2)
print ("output test_01-->", s)
print ("output test_02_a-->", s.i)
print ("output test_02_b-->", s.j)
