import ctypes
# Test ctypes.CField...
class DATASET:
    def __init__(self, version, pdata):
        self.version = version
        self.pdata = pdata

DATASET_P = ctypes.POINTER(DATASET)

class DATASET_INTERNAL:
    _fields_ = [("pdata", ctypes.CField, lambda self: self.pdata)] #but self is undefined!
    
di = DATASET_INTERNAL()
di.pdata = ctypes.pointer(DATASET(1.0, None))
print di.pdata
     
# Test ctypes.CField of nested structure       
class API:
    pass

API._fields_ = [("dataset", ctypes.CField, lambda self: self.dataset)]

api = API()
v1 = DATASET(1.0, None)
v2 = DATASET(2.0, None)
api.dataset = v1
print "api.dataset.version", api.dataset.version

