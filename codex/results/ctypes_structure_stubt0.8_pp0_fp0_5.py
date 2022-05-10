import ctypes

class S(ctypes.Structure):
    x = ctypes.c_void_p
    y = ctypes.c_void_p

s = S.in_dll(ctypes.PyDLL(None), 's')
print ctypes.cast(s.x, ctypes.c_long)
print ctypes.cast(s.x, ctypes.c_long).value
</code>
The example is taken from here.
For completeness, here's the modified version of the original code:
<code>import ctypes

def example_function():
    return 42

if __name__ == '__main__':
    lib = ctypes.PyDLL(None)

    example_function_ptr = lib.example_function
    example_function_ptr.argtypes = []
    example_function_ptr.restype = ctypes.c_int

    print example_function_ptr()
</code>

