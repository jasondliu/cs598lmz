import ctypes
FUNTYPE = ctypes.CFUNCTYPE(None, ctypes.c_int, ctypes.c_int)

def func(x, y):
    print 'x=%d, y=%d' % (x, y)

f = FUNTYPE(func)
f(1, 2)

# 在Python中，调用函数的参数可以有默认值，比如：
def func(x, y=2):
    print 'x=%d, y=%d' % (x, y)

# 如果要调用上述函数，可以只传入一个参数：
func(1)

# 如果在C语言中调用这个函数，必须传入两个参数，否则就会
