import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_double, ctypes.c_double)

def make_callback(func):
    # print "make_callback(%s)" % (func,)
    cb = FUNTYPE(func)
    return cb

def callback_test(func):
    cb = make_callback(func)
    res = cb(1.5)
    print "callback_test(%s) => %s" % (func, res)
    return res

def add_callback(func):
    cb = make_callback(func)
    lib.add_callback(cb)

def test():
    callback_test(lambda x: x*2)
    callback_test(lambda x: x**2)
    callback_test(lambda x: x+x)
    add_callback(lambda x: x*2)
    add_callback(lambda x: x**2)
    add_callback(lambda x: x+x)
    lib.run_callbacks()
