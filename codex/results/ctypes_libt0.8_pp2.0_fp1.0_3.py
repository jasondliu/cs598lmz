import ctypes
ctypes.c_uint32

# manually initializing the ctypes variables
#a = ctypes.c_uint32(5)
#b = ctypes.c_uint32(5)

# using the initializer to set the ctypes variables
a = ctypes.c_uint32(5).value
b = ctypes.c_uint32(5).value

# mutiplying the variables
print('a * b = ', a * b)

#a.value = 5
#b.value = 5
print('a * b = ', a * b)

"""

"""
# from_buffer
# from_buffer_copy
# from_address
# from_param
# from_address

# struct_time is a structure class
# which is a collection of various data types
x = time.struct_time((2014, 7, 1, 17, 3, 38, 1, 182, 0))
print (x, type(x), x.n_fields)

# converting the tuple into a buffer
buf = ctypes.create_string_buffer(x, 32)
print (buf,
