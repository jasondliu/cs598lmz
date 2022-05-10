from _struct import Struct
s = Struct.__new__(Struct)
s.format = 'i'
s.size = 4
s.pack(3)

# test __new__
# x.__new__(y) is the same as
# type(x).__new__(y)

class A(object):
    pass

a = A()
