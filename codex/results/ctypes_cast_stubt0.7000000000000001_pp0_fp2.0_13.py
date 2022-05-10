import ctypes
ctypes.cast(x, ctypes.py_object).value

# If you don't have ctypes and sys.getsizeof() doesn't work, then you might
# be able to use a function like this:
def sizeof(x):
    return len(x.encode('utf-8')) * 8
</code>

