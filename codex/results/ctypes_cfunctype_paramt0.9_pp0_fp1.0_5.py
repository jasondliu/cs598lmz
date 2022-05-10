import ctypes
FUNTYPE = ctypes.CFUNCTYPE(
    ctypes.c_void_p,
    ctypes.c_char_p, ctypes.c_int, ctypes.c_int, ctypes.c_void_p
)
allocated_objects = []
def destroy_string(ptr, len, size, userdata):
    global allocated_objects
    del allocated_objects[allocated_objects.index(ptr)]

g_destroy_string = FUNTYPE(destroy_string)
def wrapped_string(data):
    global allocated_objects
    ptr = ctypes.cast(ctypes.c_char_p(data), ctypes.c_void_p).value
    allocated_objects.append(ptr)
    return ptr, len(data), 1, g_destroy_string

klass = classObj('SomeClass')
klass.props = {'s': str}
klass.methods = [('is_blank', bool, [str]),
                 ('return_str', str, [str]),
                 ('hello_world', None, []),
                 ('echo_int', int, [int]),
                 ('
