import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int, ctypes.c_int)
def func(x, y):
    return x + y
func_c = FUNTYPE(func)
print(func_c(1, 2))

class Point(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int),
                ('y', ctypes.c_int)]

def func2(x, y):
    return x + y
func2_c = FUNTYPE(func2)
print(func2_c(Point(1, 2), Point(3, 4)))

# 使用Python示例：回调示例
class Callback:
    def __init__(self):
        self.callback_map = {}

    def register(self, name, func):
        if name in self.callback_map:
            raise Exception('callback name exists')
        self.callback_map[name] = func

    def deregister(self, name):
        if name not in self
