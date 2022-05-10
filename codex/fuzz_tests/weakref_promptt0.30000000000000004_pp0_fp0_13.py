import weakref
# Test weakref.ref()

class A:
    pass

a = A()
r = weakref.ref(a)
print(r())

del a
print(r())

class B:
    pass

b = B()
r = weakref.ref(b)
print(r())

b = 'spam'
print(r())

class C:
    pass

c = C()
r = weakref.ref(c)
print(r())

c.attr = 42
print(r())

del c.attr
print(r())

del c
print(r())

# Test weakref.proxy()

class D:
    pass

d = D()
p = weakref.proxy(d)
print(p)

del d
try:
    print(p)
except ReferenceError:
    print('ReferenceError')

class E:
    pass

e = E()
p = weakref.proxy(e)
print(p)

e = 'spam'
try:
    print(p)
except ReferenceError
