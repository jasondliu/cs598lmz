import weakref
# Test weakref.ref()
class A:
  pass
a = A()
aref = weakref.ref(a)
aref

import sys
print(sys.getrefcount(a))

aref() is a

print(sys.getrefcount(a))

del a
print(sys.getrefcount(a))


import weakref
s1 = {1, 2, 3}
s2 = s1
def bye():
    print('Gone with the wind...')

ender = weakref.finalize(s1, bye)
ender.alive
del s1
ender.alive
s2 = 'spam'

x = 42
x = 'shrubbery'
x = 3.1415
x = None

x
x = 'shrubbery'
x

x = None
x
x = 'shrubbery'

L1 = [2, 3, 4]
L2 = L1
L2
del L1
L2

L1 = 42

L1 = [2, 3, 4]
L2 = L1

