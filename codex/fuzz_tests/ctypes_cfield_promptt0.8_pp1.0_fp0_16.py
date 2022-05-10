import ctypes
# Test ctypes.CField.

class S(ctypes.Structure):
    _fields_ = [('i', ctypes.c_int)]

class C(ctypes.Structure):
    _fields_ = [('s', S)]

s = S()
c = C()

c.s = s
print(c.s.i)
s.i = 42
print(c.s.i)
c.s.i = 12
print(s.i)

# make sure that we can use a Structure subclass

class SubS(S):
    _fields_ = [('l', ctypes.c_long)]

class SubC(C):
    _fields_ = [('s', SubS)]

subs = SubS()
subc = SubC()

subc.s = subs
print(subc.s.i, subc.s.l)
subs.i = 99
print(subc.s.i, subc.s.l)
subs.l = 100000
print(subc.s.i, subc.s.l)
