import ctypes
ctypes.cast(0, ctypes.py_object).value

# 创建一个类型为c_int的数组，数组长度为5
array_type = ctypes.c_int * 5
ia = array_type(1, 2, 3, 4, 5)
print(ia)
print(ia[0])
print(ia[1])
print(ia[2])
print(ia[3])
print(ia[4])

# 创建一个类型为c_char_p的数组，数组长度为5
array_type = ctypes.c_char_p * 5
ia = array_type(b'a', b'b', b'c', b'd', b'e')
print(ia)
print(ia[0])
print(ia[1])
print(ia[2])
print(ia[3])
print(ia[4])


