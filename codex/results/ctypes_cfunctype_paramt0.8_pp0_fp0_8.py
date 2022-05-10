import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int, ctypes.c_int)

class MethodWrapper:
    def __init__(self, callback):
        self.callback = callback

    def __call__(self, a, b):
        return self.callback(a, b)

class Callback:
    def __init__(self, callback):
        self.callback = FUNTYPE(callback)

    def __call__(self, a, b):
        return self.callback(a, b)

def add_ints(a, b):
    return a + b

def add(a, b):
    return a + b

def mul(a, b):
    return a * b

def sub(a, b):
    return a - b

def twospace(f):
	def func(a, b):
		return f(a, b) + f(a, b)
	return func

if __name__ == "__main__":
    print(add_ints(4, 5))
    print(Callback(add)(4
