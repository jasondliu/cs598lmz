import ctypes
FUNTYPE = ctypes.CFUNCTYPE(None, ctypes.c_int, ctypes.c_int, ctypes.c_int, ctypes.c_int, ctypes.c_int)

# define a global function outside the class
def GLOBAL_CALLBACK(x, y, button, action, mods):
    print("GLOBAL_CALLBACK: x = %d, y = %d, button = %d, action = %d, mods = %d" % (x, y, button, action, mods))

# define a class with a static method as the callback
class CallbackClass:
    @staticmethod
    def STATIC_CALLBACK(x, y, button, action, mods):
        print("STATIC_CALLBACK: x = %d, y = %d, button = %d, action = %d, mods = %d" % (x, y, button, action, mods))

# define a class with an instance method as the callback
class CallbackObject:
    def __init__(self):
        pass
    def INSTANCE_CALLBACK(self, x, y,
