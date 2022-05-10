import ctypes

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CField = type(S.x)

try:
    x = ctypes.CField
    assert x == type(S.x) and x != ctypes.c_int
except:
    py.test.skip("AppDirect mode not supported")

result = S()
result.x = 11
serialized = pickle.dumps(S.x)
result2 = pickle.loads(serialized)
assert result.x == 11
result.x = 22
result2.x = 33
assert result.x == 33
result.x = 44
assert result2.x == 44
