import ctypes

class S(ctypes.Structure):
    x = struct_float33()

o = S()
o.x = (1.0, (2.0, 3.0, 4.0), (5.0, 6.0, 7.0))

result = m.S_float33_fn(o)
print("S_float33_fn(", o, ")=", result)

s = m.S_float33()
s.x = (1.0, (2.0, 3.0, 4.0), (5.0, 6.0, 7.0))

result = m.S_float33_fn2(s)
print("S_float33_fn(", s, ")=", result)
