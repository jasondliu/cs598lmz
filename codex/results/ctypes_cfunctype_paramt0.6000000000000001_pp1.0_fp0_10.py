import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_double, ctypes.c_double)

def func(x):
    return x ** 2

# Numpy array to pointer
arr = np.arange(10, dtype=np.float64)
arr_p = arr.ctypes.data_as(ctypes.POINTER(ctypes.c_double))

# Function pointer to Python function
f = FUNTYPE(func)

# Call external C function
result = _lib.cfunc(f, arr_p, len(arr))

# Output
print(result)
print(arr)

# Clean up
del result
del arr
del arr_p
</code>
Output:
<code>9.0
[0. 1. 4. 9. 16. 25. 36. 49. 64. 81.]
</code>
My question is:
What is the best way to handle the memory management of the <code>arr</code> array, considering that the <code>cfunc</code> function may be called several times?
I would like to avoid doing a <code>del arr</code> after each
