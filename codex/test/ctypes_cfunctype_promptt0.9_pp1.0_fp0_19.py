import ctypes
# Test ctypes.CFUNCTYPE passing/returning Py_buffer and/or a raw pointer.
# This requires passing all the information to ctypes in this function.
# Used by test_buffer_type()
def BufferCallback(py_buffer, buf_len, some_int, pbuf):
    assert some_int == 4
    assert pbuf.value == 42
    assert pbuf[:buf_len] == b'Hello World'
    return py_buffer.obj

