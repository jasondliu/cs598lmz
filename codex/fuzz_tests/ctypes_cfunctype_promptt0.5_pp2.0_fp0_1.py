import ctypes
# Test ctypes.CFUNCTYPE
def dummy_callback(x, y):
    print x, y

dummy_callback_type = ctypes.CFUNCTYPE(None, ctypes.c_int, ctypes.c_int)
dummy_callback_func = dummy_callback_type(dummy_callback)
dummy_callback_func(1, 2)

# Test ctypes.c_void_p.from_param
class Dummy(object):
    def __init__(self, value):
        self.value = value
    def __int__(self):
        return self.value

dummy_instance = Dummy(123)
dummy_instance_addr = ctypes.c_void_p.from_param(dummy_instance)
print int(dummy_instance_addr)

# Test ctypes.c_char_p.from_param
dummy_str = 'hello'
dummy_str_addr = ctypes.c_char_p.from_param(dummy_str)
print dummy_str_addr

# Test ctypes.c_char_
