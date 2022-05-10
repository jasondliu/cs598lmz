fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi.gi_code
fn.__code__

# copy_reg
import copy_reg
import types

def reduce_method(m):
    return (getattr, (m.im_class, m.im_func.func_name))
copy_reg.pickle(types.MethodType, reduce_method)

class C(object):
    def __init__(self, x=1):
        self.x = x
    def spam(self, y):
        print("C.spam", self.x, y)
c = C()
import pickle
pickled = pickle.dumps(c.spam)
pickled
pickle.loads(pickled)

# marshal
import marshal
assert marshal.dumps(1) == 'i\x01\x00\x00\x00'
assert marshal.dumps(1.0) == 'g\x00\x00\x00\x00\x00\x00\xf0?'
assert marshal.dumps(1j) == 'g\x00\x00
