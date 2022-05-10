import ctypes
# Test ctypes.CField
#
# An important property of ctypes is that it can be used to set and get
# arbitrary memory locations.
# CFields provide an interface to access
# struct fields.
#
# The struct module can be used to define a C compatible struct, and then
# string instances can be mapped onto the fields of the struct.
# The following example uses the struct module to create a 4 byte
# representation of an integer value, access it using ctypes,
# change the value, and convert the result back to an integer.
#
# Note:
# This is a very low level interface,
# so be careful when using it.

values = [0x12345678]

fmt = "L"
size = struct.calcsize(fmt)

if size != ctypes.sizeof(ctypes.c_long):
    print("sizeof(long) doesn't equal %d" % size)
else:
    print("sizeof(long) equals %d" % size)


# Setup a buffer
s = struct.Struct(fmt)
buf = s.pack(*values)

for
