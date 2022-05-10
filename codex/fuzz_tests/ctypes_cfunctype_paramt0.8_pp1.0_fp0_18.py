import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object ,ctypes.py_object)

inval = sys.intern("inval")
run = sys.intern("run")
ok = sys.intern("ok")
fail = sys.intern("fail")
todo = sys.intern("todo")
skip = sys.intern("skip")
add_skip = sys.intern("add_skip")
add_inval = sys.intern("add_inval")

restrictions = {
    "skip": None,
    "inval": None,
    "run": None,
}

def abort():
    #XXX probably we should print an error message for the user
    sys.exit(1)

def validate_restriction(name):
    if not (name == "skip" or name == "inval" or name == "run"):
        abort()

class test(object):
    name = None
    func = None
    todo = None
    target = None
    args = None
    kwargs = None
    def __init__(self, name = None, func = None, to
