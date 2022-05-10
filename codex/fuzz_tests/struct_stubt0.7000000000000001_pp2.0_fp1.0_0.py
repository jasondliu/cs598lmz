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
print type(a)
print type(a).__mro__

class B(A):
    pass
b = B()
print type(b)
print type(b).__mro__

class C(object):
    pass
c = C()
print type(c)
print type(c).__mro__

#type(c).__new__(A) # TypeError: __new__() should return an instance of C, not A


class D(B, C):
    pass
d = D()
print type(d)
print type(d).__mro__

class E(B, A):
    pass
e = E()
print type(e)
print type(e).__mro__

class F(B):
    pass

