from _struct import Struct
s = Struct.__new__(Struct)

#print(type(s))

#print(s._fields_)

try:
    s = Struct('abcdef')
except Exception as e:
    print(e)

try:
    s = Struct('10s 10s')
except Exception as e:
    print(e)

s = Struct('10s 10s')
print(s.size)


s = Struct('i')
s.pack(123)
print(s.pack(123))
