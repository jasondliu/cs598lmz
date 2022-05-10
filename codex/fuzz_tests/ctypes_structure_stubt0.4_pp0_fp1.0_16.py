import ctypes

class S(ctypes.Structure):
    x = ctypes.c_longlong
    y = ctypes.c_longlong

print S.x
print S.y
print S.__dict__
print S.__dict__['x']
print S.__dict__['y']

print S.x.__dict__
print S.y.__dict__
print S.x.__dict__['offset']
print S.y.__dict__['offset']

print S.x.__dict__['offset'] == 0
print S.y.__dict__['offset'] == 8

print S.x.__dict__['offset'] == 0
print S.y.__dict__['offset'] == 8

print S.x.__dict__['offset'] == 0
print S.y.__dict__['offset'] == 8

print S.x.__dict__['offset'] == 0
print S.y.__dict__['offset'] == 8

print S.x.__dict__['offset'] == 0
print S.y.__dict__['offset'] == 8

print S.x.__dict__['
