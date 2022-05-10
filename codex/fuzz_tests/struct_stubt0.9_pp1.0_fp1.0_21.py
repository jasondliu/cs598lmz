from _struct import Struct
s = Struct.__new__(Struct)
s.__setattr__('_fmt', 'dddd')
f = s.unpack_from

q1, q2, q3, q4 = f(msg, 8)
print(q1, q2, q3, q4)
