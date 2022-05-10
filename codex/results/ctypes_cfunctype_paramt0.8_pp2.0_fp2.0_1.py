import ctypes
FUNTYPE = ctypes.CFUNCTYPE(None)
class PyFunCall:
    def __init__(self,fun):
        self.fun = fun
        self.ctypes_fun = FUNTYPE(fun)
    def __call__(self):
        self.ctypes_fun()
def fun1(fun):
    def fun2():
        print("开始执行")
        fun()
        print("结束执行")
    return fun2
@fun1
def f1():
    print("连接数据库")
@fun1
def f2():
    print("查询数据库")
def test():
    f1()
    f2()
if __name__ == '__main__':
    test()
