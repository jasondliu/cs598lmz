import ctypes
FUNTYPE = ctypes.CFUNCTYPE(None, ctypes.c_int)
def pyfunc(arg):
    print(arg)
cfunc = FUNTYPE(pyfunc)
cfunc(110)

# 当Python解释器退出时，它会搜索留存的对象，如果发现某个对象是ctypes模块创建的
# 类实例，并且对象包含一个资源（如内存、文件或网络连接），解释器就会自动释放该资源
# 这就是为什么你无需手动释放ctypes分配
