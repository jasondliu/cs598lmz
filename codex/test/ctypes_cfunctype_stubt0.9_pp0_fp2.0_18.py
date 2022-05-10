import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    print("fun()")
    return None

def test(argtypes, args):
    for obj in args:
        for argtype in argtypes:
            try:
                fun(argtype(obj))
                print("ok: %s(%r)" % (argtype, obj))
            except:
                print("--: %s(%r)" % (argtype, obj))


for argtype in [ctypes.c_char, ctypes.c_wchar]:
    print("-------------")
