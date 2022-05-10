import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    return 1

def fun_dec(f):
    @wraps(f)
    def fun():
        return 1
    return fun

#class fun_dec(object):
#    def __init__(self, f):
#        self.f = f
#    def __call__(self, *args, **kwargs):
#        return 1

def fun_dec2(f):
    def fun():
        return 1
    return fun

def dec_fun_dec(f):
    #@wraps(f)
    def dec_f(*args, **kwargs):
        return 1
    return dec_f

@dec_fun_dec
def fun_with_dec():
    return 1


if __name__ == "__main__":
    #print(fun_with_dec() == 1)
    print(fun())
    #print(fun() == 1)
    #print("orginal doc:", fun.__doc__)
    #print("doc with dec:", fun_dec.__doc__)
    #print("doc with dec
