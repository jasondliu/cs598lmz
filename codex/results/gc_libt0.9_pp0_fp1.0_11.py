import gc, weakref
import numpy as np

class MyObj(object):
    def __init__(self):
        x = np.zeros((100,10))
        x = 1.0
        print "Born"

def died(x = None):
    print "Die"

obj = MyObj()
ref = weakref.ref(obj, died)
print ref, ref()
assert ref() is obj
del obj
gc.collect()
assert ref() is None
 
print ref, ref()
