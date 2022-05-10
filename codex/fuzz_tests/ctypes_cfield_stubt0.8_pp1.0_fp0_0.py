import ctypes

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CField = type(S.x)
</code>
However, this fails to pickle dicts containing instances of the class S:
d = {'s': S()}
pickle.dumps(d)
TypeError: can't pickle ctypes.CField objects

