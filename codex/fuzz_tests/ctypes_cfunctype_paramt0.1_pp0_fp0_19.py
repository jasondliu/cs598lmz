import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int)

def my_callback(x):
    print("my_callback called with %d" % x)
    return x + 1

my_callback_c = FUNTYPE(my_callback)

my_callback_c(1)

# my_callback_c is now a ctypes function type
print(my_callback_c)

# my_callback_c is now a ctypes function type
print(my_callback_c)

# my_callback_c is now a ctypes function type
print(my_callback_c)

# my_callback_c is now a ctypes function type
print(my_callback_c)

# my_callback_c is now a ctypes function type
print(my_callback_c)

# my_callback_c is now a ctypes function type
print(my_callback_c)

# my_callback_c is now a ctypes function type
print(my_callback_c)

# my_callback_c is now a ctypes function type
print(
