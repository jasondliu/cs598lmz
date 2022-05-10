import ctypes

class S(ctypes.Structure):
    x = 10

s = S()

print(s['x'], type(s['x']))
print(dir(s['x']))
print(dir(s['x']._set(12)))

try:
    s['x'] = 11
except AttributeError as e:
    print(type(e), e)
