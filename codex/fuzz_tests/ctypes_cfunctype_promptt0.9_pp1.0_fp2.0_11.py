import ctypes
# Test ctypes.CFUNCTYPE() by creating the equivalent of this Python function
#
# def string_at(count, handle):
#    buf = create_string_buffer(count)
#    string_at_func(buf, count, handle)
#    return buf.value
#
# Note: string_at_func() doesn't actually exist.

STRING_AT_FUNC = ctypes.CFUNCTYPE(
    None, ctypes.POINTER(ctypes.c_char), ctypes.c_int, ctypes.py_object)

def string_at(count, handle):
    buf = create_string_buffer(count)
    string_at_func(buf, count, handle)
    return buf.value

# The reverse of string_at().

def string_at_reverse(buf, handle):
    string_at(len(buf), handle)

# Test CFUNCTYPE() with callbacks in a struct
#
# struct CALLBACKS {
#    int (*sum)(int, int);
#    void (*nothing)(void);
#    char* (*string_
