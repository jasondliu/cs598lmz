import ctypes
# Test ctypes.CField.from_address Method
p = lib.get_point()
print(p.x, p.y)  # output: 123 456

######################################################################
## Here is how to set fields using ctypes.CField.from_address Method

# Test ctypes.CField.from_address Method
p = lib.get_point()
print(p.x, p.y)

c_int.from_address(ctypes.addressof(p), 0).contents.value = 456
c_int.from_address(ctypes.addressof(p), 1).contents.value = 123

print(p.x, p.y)
######################################################################

# Test ctypes.Structure.from_address Method                                         
p = lib.get_point()
print(p.x, p.y)

point.from_address(ctypes.addressof(p)).x = 9999
print(p.x, p.y)                                         

# Test ctypes.Structure.from_buffer_copy Method                                         
# The
