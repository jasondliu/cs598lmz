import ctypes
ctypes.cast(0, ctypes.py_object).value

# 从内存指针恢复对象
ctypes.cast(id(5), ctypes.c_void_p).value

# 利用ctypes实现多线程
def func(i):
    print('hello world', i)

# 创建多个线程
for i in range(10):
    t = threading.Thread(target=func, args=(i,))
    t.start()

# 创建多个线程，利用ctypes
libc = ctypes.CDLL(None)
# 新建线程
CMPFUNC = ctypes.CFUNCTYPE(ctypes.c_void_p, ctypes.c_void_p)
def thread_body(a):
    print('hello world', ctypes.cast(a, c
