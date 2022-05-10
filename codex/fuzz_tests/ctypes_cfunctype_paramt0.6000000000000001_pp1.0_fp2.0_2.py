import ctypes
FUNTYPE = ctypes.CFUNCTYPE(None,ctypes.c_int)

class Test(object):
    def __init__(self):
        self.g_fun = FUNTYPE(self.fun_a)
        self.b_fun = None

    def fun_a(self, a):
        print a

    def fun_b(self, a):
        print a
        self.b_fun = FUNTYPE(self.fun_a)
        self.g_fun = self.b_fun


if __name__ == '__main__':
    test = Test()
    test.g_fun(1)
    test.g_fun(2)
    test.b_fun(3)
    test.g_fun(4)
</code>
The result of this is:
<code>1
2
3
4
</code>

