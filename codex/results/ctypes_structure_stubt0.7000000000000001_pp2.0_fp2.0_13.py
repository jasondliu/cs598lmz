import ctypes

class S(ctypes.Structure):
    x = ctypes.c_int
    y = ctypes.c_int

s = S()
s.x = 3
s.y = 4

print s.x
print s.y

print S.x.offset

# use string to represent the member name
print S.x.offset == getattr(S, 'x').offset

# use string to represent the member name
print S.x.offset == S.__dict__['x'].offset

# use string to represent the member name
print S.x.offset == S.__dict__.get('x').offset

# use string to represent the member name
print S.x.offset == getattr(S, '_fields_')[0][1].offset

# use string to represent the member name
print S.x.offset == getattr(S, '_fields_')[0][1].offset

# use string to represent the member name
print S.x.offset == getattr(S, '_fields_')[0][1].offset

# use string to represent the member name
print S.x.
