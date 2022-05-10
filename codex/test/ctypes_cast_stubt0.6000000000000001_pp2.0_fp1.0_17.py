import ctypes
ctypes.cast(None, ctypes.py_object)

# dummy test, just to make sure ctypes is working

def test_1():
    global lib_handle
    lib_handle = ctypes.CDLL(None)
    assert(lib_handle)


# test that ctypes works with a shared library

def test_2():
    global lib_handle
    global lib_handle2
    lib_handle = ctypes.CDLL('libc.dylib')
    assert(lib_handle)
    lib_handle2 = ctypes.CDLL('libc.dylib')
    assert(lib_handle2)
    assert(lib_handle == lib_handle2)


# test that ctypes works with a shared library, with a name

def test_3():
    global lib_handle
    global lib_handle2
    lib_handle = ctypes.CDLL('libc.dylib', 'libc.dylib')
    assert(lib_handle)
    lib_handle2 = ctypes.CDLL('libc.dylib', 'libc.dylib')
    assert(lib_handle2)
