import weakref
# Test weakref.ref()
import sys

class A:
    pass

class B:
    pass

a = A()
b = B()
c = a
wr = weakref.ref(b)

print(wr.__call__())
print(wr())

print(wr.__hash__() == hash(b))
print(hash(wr) == hash(b))

print(wr.__eq__(b))
print(wr == b)

print(wr.__ne__(b))
print(wr != b)

print(wr.__ne__(a))
print(wr != a)

#print(wr.__lt__(a))
#print(wr < a)

#print(wr.__le__(a))
#print(wr <= a)

#print(wr.__gt__(a))
#print(wr > a)

#print(wr.__ge__(a))
#print(wr >= a)

print(wr.__repr__())
print(repr(wr))

print(wr.__str
