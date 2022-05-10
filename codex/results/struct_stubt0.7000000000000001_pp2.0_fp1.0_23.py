from _struct import Struct
s = Struct.__new__(Struct)
s.__delattr__("format")

class Dict(dict):
    def __init__(self, x={}, **kwargs):
        self.update(x)
        self.update(kwargs)
    def __setitem__(self, k, v):
        super(Dict, self).__setitem__(k, v)
        self.__dict__[k] = v
