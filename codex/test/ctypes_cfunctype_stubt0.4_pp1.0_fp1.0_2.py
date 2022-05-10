import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    return 1

def f():
    return fun()

def g():
    return f()

def h():
    return g()

def run_direct(count):
    for i in range(count):
        fun()

def run_indirect_f(count):
    for i in range(count):
        f()

def run_indirect_g(count):
    for i in range(count):
        g()

def run_indirect_h(count):
    for i in range(count):
        h()

def entry_point(argv):
    run_direct(int(argv[1]))
    run_indirect_f(int(argv[1]))
    run_indirect_g(int(argv[1]))
    run_indirect_h(int(argv[1]))
    return 0

def target(*args):
    return entry_point, None

