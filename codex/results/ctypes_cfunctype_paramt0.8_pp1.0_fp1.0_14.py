import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_bool, ctypes.c_int, ctypes.c_void_p)
cfunc = CFUNCTYPE(ctypes.c_bool, ctypes.c_int, ctypes.c_void_p)
cfunc(self.dev_handle, ctypes.pointer(data), 1000, c_callback, ctypes.POINTER(user_data))
</code>
EDIT:
I tried another approach:
I added a class with a static method as callback. The callback method is in the same class as the main application:
<code>class StaticCallbackClass(object):

    def __init__(self, parent):
        self.parent = parent

    @staticmethod
    def callback_method(data, data2):
        print("callback method called")
        print("data1: {}".format(data))
        print("data2: {}".format(data2))

    def call_function(self):
        data = ctypes.c_uint64(10)
        data2 = ctypes.c_int(20)
        static_callback_method = cfunc
