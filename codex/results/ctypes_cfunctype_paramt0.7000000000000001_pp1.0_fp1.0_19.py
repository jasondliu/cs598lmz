import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_double, ctypes.c_double)

# a simple function that divides by two
@FUNTYPE
def half(x):
    return x / 2.0

half(6.0)

# a function that takes two parameters and a function
@FUNTYPE
def apply_func(x, f):
    return f(x)

# a more complex function that divides by two
@FUNTYPE
def half_complex(x):
    return 1 / (1 + math.exp(-x))

# call apply_func with a function pointer to half_complex
result = apply_func(6.0, half_complex)

# we can also assign the function pointer to a variable
# and pass that variable as an argument
f = FUNTYPE(half_complex)
result = apply_func(6.0, f)
</code>

