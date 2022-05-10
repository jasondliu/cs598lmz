import ctypes
ctypes.cast(object, type)

def get_ctypes_pointer(obj):
    return ctypes.cast(obj, ctypes.POINTER(ctypes.c_float))

def get_ctypes_array(obj):
    return get_ctypes_pointer(obj.ctypes.data)

def get_ctypes_array_slice(obj, start, end):
    return (ctypes.c_float * (end - start))(get_ctypes_array(obj)[start:end])

def get_ctypes_array_slice_pointer(obj, start, end):
    return ctypes.cast(get_ctypes_array_slice(obj, start, end), ctypes.POINTER(ctypes.c_float))

def get_ctypes_array_pointer(obj):
    return ctypes.cast(obj.ctypes.data, ctypes.POINTER(ctypes.c_float))

def get_ctypes_array_pointer_slice(obj, start, end):
    return ctypes.cast(get_ctypes_array(obj)[start:end],
