import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_void_p)

class Test:
    def __init__(self):
        self.s = "hello world"
        self.f = FUNTYPE(self.callback)
        self.p = ctypes.c_void_p()

    def callback(self, p):
        print(self.s)
        return 0

    def test(self):
        print("test")
        return 0

def create_callback(obj):
    return FUNTYPE(obj.callback)

def create_test(obj):
    return FUNTYPE(obj.test)

def main():
    t = Test()
    t.callback(t.p)
    t.f(t.p)
    t.f = create_callback(t)
    t.f(t.p)
    t.f = create_test(t)
    t.f(t.p)

if __name__ == '__main__':
    main()
</code>

