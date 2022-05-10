import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_double, ctypes.c_double, ctypes.c_double)

def run_test(name, func, arg1, arg2, expected):
    print("Expecting %s(%s, %s) = %s" % (name, arg1, arg2, expected))
    result = func(arg1, arg2)
    print("Got %s" % result)
    if result != expected:
        raise Exception("Test %s failed!" % name)

@FUNTYPE
def add(arg1, arg2):
    return arg1 + arg2

@FUNTYPE
def sub(arg1, arg2):
    return arg1 - arg2

@FUNTYPE
def mul(arg1, arg2):
    return arg1 * arg2

@FUNTYPE
def div(arg1, arg2):
    return arg1 / arg2

@FUNTYPE
def sin(arg1, arg2):
    return math.sin(arg1)

@FUNTYPE
def cos(arg1, arg2):
    return math.cos(arg1
