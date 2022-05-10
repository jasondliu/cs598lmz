import ctypes
# Test ctypes.CFUNCTYPE
# addOne = ctypes.cdll.LoadLibrary('libadd_one.so')
# b = ctypes.c_int32(1)
# c = addOne.AddOne()
# print(c)
print('-'*20)

# Test
# a = 0xAAAA
# b = ctypes.c_int32(a)
# print(hex(b.value))
# print(type(b.value))

# print('-'*20)
# str1 = "hello world"
# str2 = ctypes.c_char_p(str1)
# print(str2)
# print(str2.value)
# print(type(str2))
# print(type(str2.value))

print('-'*20)
h1 = int('0xffff',16)
h1 = ctypes.c_int32(h1)

h2 = int('0xffff',16)
h2 = ctypes.c_int32(h2)

h3 = h1.value*h2.value
