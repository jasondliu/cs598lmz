import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_void_p, ctypes.c_void_p, ctypes.c_void_p)

class Head(object):
    def __init__(self, name):
        self.name = name
    def __enter__(self):
        self.head = mlpack.head(*args, ostream=None)
        return self.head
    def __exit__(self, *etc):
        self.head = None
        return
 
class NumPyHead(object):
    def __init__(self, name):
        self.name = name
    def __enter__(self):
        return self.name
    def __exit__(self, *etc):
        return

class StructuredHead(object):
    def __init__(self, name, structure):
        self.name = name
        self.structure = structure
    def __enter__(self):
        return self.structure
    def __exit__(self, *etc):
        self.structure = None
        return

class StructuredHeadFromMLPACK(object):

