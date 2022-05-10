import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    return None

def f():
    return fun()

def g():
    return f()

def h():
    return g()

def main():
    h()

main()
""")

    def test_call_with_kwargs(self):
        self.run_test("""
def fun(a, b, c):
    return a, b, c

def f():
    return fun(a=1, b=2, c=3)

def main():
    return f()

print(main())
""", "1, 2, 3")

    def test_call_with_kwargs_and_defaults(self):
        self.run_test("""
def fun(a, b, c=3):
    return a, b, c

def f():
    return fun(a=1, b=2)

def main():
    return f()

print(main())
