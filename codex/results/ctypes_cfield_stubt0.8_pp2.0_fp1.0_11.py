import ctypes

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CField = type(S.x)

class CField(ctypes.CField):
    def __get__(self, inst, cls):
        if inst is None:
            return self
        return self.from_address(inst)

    def __set__(self, inst, value):
        self.from_address(inst).value = value

S._fields_ = [('x', CField)]

#----------------------------------------------------------------------------------------------#

def callback(fmt):
    names = []
    for item in fmt:
        if not isinstance(item, str):
            raise Exception("Bad format string")
        if item == '!':
            names.append('retval')
        else:
            names.append(item)
    return ctypes.CFUNCTYPE(ctypes.c_int, *((ctypes.c_int,) * len(names)))(lambda *args: dict(zip(names, args)))

class Callback(object):
    def __init__(self, *args):
        self.__dict__['callback_type'] = callback(args)

    def __call__(self
