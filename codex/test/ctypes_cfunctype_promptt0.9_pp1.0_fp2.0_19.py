import ctypes
# Test ctypes.CFUNCTYPE, ctypes.c_int, ctypes.c_void_p
def callback(i, msg):
    print("in callback(), i = %d, msg = %s"%(i, msg.value.decode("utf-8")))

C_CB = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int, ctypes.c_void_p)

#p = C_CB(callback)
#dll.use_callback_func(p, ctypes.c_int(1), ctypes.c_char_p("I am from python".encode("utf-8")))

# Test ctypes.POINTER, POINTER(ctypes.c_char_p)
class ARRAY_STR(ctypes.Structure):
    _fields_ = [("count", ctypes.c_int), ("arr", ctypes.POINTER(ctypes.c_char_p))]

a = ARRAY_STR()

