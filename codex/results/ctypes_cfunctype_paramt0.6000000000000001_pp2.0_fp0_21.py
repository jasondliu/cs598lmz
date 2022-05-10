import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_double, ctypes.c_double)

def pow(x):
    return x**2

pow_func = FUNTYPE(pow)
print(pow_func(2))

def hum(x):
    return x+3
hum_func = FUNTYPE(hum)
print(hum_func(3))



# 回调函数
# 设置回调函数
def callback(arg):
    print('callback {}'.format(arg))

def myfunc(func):
    print('myfunc')
    func('hello')

myfunc(callback)

# 定义回调函数
def callback(arg, func):
    print('callback {}'.format(arg))
    func('hello')

# 定义回调函数
def callback2(arg):
    print('callback2 {}'.format(arg))

def myfunc(func):
    print('myfunc')
    func('
