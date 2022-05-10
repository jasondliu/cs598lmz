import ctypes
ctypes.cast(result_buffer, ctypes.POINTER(int32pointer_t))[0] # you get a ctypes.POINTER, but I want the value it points to.
print(result_buffer[0])
print(np.frombuffer(result_buffer, dtype=np.int32)[0])
print(np.ctypeslib.as_array(result_buffer.obj.get_obj()))
print(result_buffer.contents)

# ==========

import ast
ast.literal_eval(''.join(('[', '1234', ']', '')))

# ==========

class MyArray(ctypes.Array):
    _type_ = ctypes.POINTER(ctypes.c_int32)  # type of the array
    _length_ = 2  # number of elements of the array


c_array = MyArray()
c_array[0] = 123
c_array[1] = 456
print(c_array[:])
