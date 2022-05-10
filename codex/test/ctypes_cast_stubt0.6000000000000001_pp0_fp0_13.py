import ctypes
ctypes.cast(ctypes.pointer(ctypes.c_int(42)), ctypes.POINTER(ctypes.c_int))

ctypes.cast(ctypes.pointer(ctypes.c_float(3.14)), ctypes.POINTER(ctypes.c_double))

#pragma: coderesponse end


#pragma: coderesponse template
def make_array(n):
    return (n * ctypes.py_object)()

#pragma: coderesponse end

#pragma: coderesponse template
def set_item_in_array(array, index, value):
    array[index] = value

#pragma: coderesponse end

#pragma: coderesponse template
def get_item_from_array(array, index):
    return array[index]

#pragma: coderesponse end
