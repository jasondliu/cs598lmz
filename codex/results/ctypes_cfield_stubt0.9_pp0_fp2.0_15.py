import ctypes

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CField = type(S.x)

class C(ctypes.CDLL):
    pass

def encode_pointer(p):
    return '%x' % ctypes.addressof(p)

def decode_pointer(r):
    return ctypes.c_void_p(int(r, 16)).value

class BridgeHandler(object):
    def __init__(self, bridge):
        self.bridge = bridge

    def handle_method(self, method, args):
        methname = method.__name__
        if methname == '__getattr__':
            second_args = args[1]
            methname = second_args[1:]
        elif methname.startswith('__'):
            methname = methname[2:-2]
        else:
            methname, _, attrname = methname.partition('_')
        try:
            meth = getattr(self, methname)
        except AttributeError:
            return method(*args)
        return meth(method, *args)

    def e(self, return_):
        try:
           
