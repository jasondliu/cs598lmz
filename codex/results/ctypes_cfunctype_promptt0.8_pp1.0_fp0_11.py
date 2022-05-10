import ctypes
# Test ctypes.CFUNCTYPE(*args)
func1 = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_char, ctypes.c_char)(lambda x, y: ord(x) + y)
assert func1('a', 3) == 97+3
assert func1(b'a', 3) == 97+3
try:
    func1(u'a', 3)
except TypeError:
    pass
else:
    raise Exception("Did not raise TypeError")

func2 = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_char, ctypes.c_char)(lambda x, y: ord(x) + y)
assert func2('a', 3) == 97+3
assert func2(b'a', 3) == 97+3
try:
    func2(u'a', 3)
except TypeError:
    pass
else:
    raise Exception("Did not raise TypeError")

# Test ctypes.CFUNCTYPE([list of argtypes], restype=int, use_errno=False)

