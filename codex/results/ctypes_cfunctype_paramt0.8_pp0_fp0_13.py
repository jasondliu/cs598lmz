import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int)


# 简单使用, 没有共享库依赖
def common_use(n):
    if n == -1:
        return -1
    if n == 0:
        return 1

    return common_use(n-1) + common_use(n-2)

# 加载共享库
def use_lib(n):
    # 动态库句柄
    handle = cdll.LoadLibrary(DLLPATH)
    # 配置函数
    func = FUNTYPE(handle.fib_c)
    # 执行函数
    res = func(n)
    return res

if __name__ == "__main__":
    use_lib(10)
