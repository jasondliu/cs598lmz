import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int, ctypes.c_int)

count = 0
def callback(a, b):
    global count
    count += a+b
    return a+b

func = FUNTYPE(callback)

for i in range(1000000):
    func(i, i+1)

print("Result: %d" % count)
