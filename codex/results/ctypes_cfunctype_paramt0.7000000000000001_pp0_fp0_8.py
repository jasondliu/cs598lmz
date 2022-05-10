import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_int,ctypes.c_int,ctypes.c_int)  # 定义函数类型
def sum_func(x,y):
    return x+y

class MClass:
    def __init__(self):
        self.sum_cbk = FUNTYPE(sum_func)
        self.sum_cbk(1,2)
        self.sum_cbk(2,3)


if __name__=='__main__':
    m = MClass()
