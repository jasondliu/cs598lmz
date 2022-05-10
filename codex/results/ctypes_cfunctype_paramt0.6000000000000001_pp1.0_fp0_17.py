import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int)
def callback(n):
    print("Callback was called with", n)
    return n

lib.register_callback(FUNTYPE(callback))
lib.run_callback(42)

# Callback with a class
class CallbackClass:
    def __init__(self):
        self.callback_id = None
        self.count = 0
    def __call__(self, n):
        print("Callback was called with", n)
        self.count += 1
        return n

cb = CallbackClass()
lib.register_callback(FUNTYPE(cb))
lib.run_callback(42)
print("Callback was called", cb.count, "times")

# Callback with a class (2)
class CallbackClass2:
    def __init__(self):
        self.callback_id = None
        self.count = 0
    def __call__(self, n):
        print("Callback was called with", n)
        self.count += 1
        return n

cb = Callback
