import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int)

def my_callback(x):
    print("my_callback", x)
    return x * 2

my_callback_c = FUNTYPE(my_callback)

# call the function
print(my_callback_c(5))

# call the function via a pointer
print(my_callback_c.__call__(5))

# call the function via a pointer
print(my_callback_c(5))

# call the function via a pointer
print(my_callback_c(5))

# call the function via a pointer
print(my_callback_c(5))

# call the function via a pointer
print(my_callback_c(5))

# call the function via a pointer
print(my_callback_c(5))

# call the function via a pointer
print(my_callback_c(5))

# call the function via a pointer
print(my_callback_c(5))

# call the function via a pointer
print(my_callback_c(5))
