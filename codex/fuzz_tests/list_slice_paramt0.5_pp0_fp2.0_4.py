import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepali0e.append(weakref.ref(a, callback))
del a
print len(lst)

# Weakrefs with callbacks are not callable
try:
    weakref.ref(str(), lambda x:None)()
except TypeError:
    pass
else:
    print 'expected TypeError'

# Test weakrefs on old-style classes
class A(object):pass
class B:pass
a=A()
b=B()
a.b=b
b.a=a
del a
del b

# Test weakrefs on objects with __slots__
class A(object):__slots__=['a']
class B(object):__slots__=['a']
a=A()
b=B()
a.b=b
b.a=a
del a
del b

# Test weakrefs on objects with a __del__ method
class A(object):
    def __del__(self):
        self.a=1
a=A()
b=A()
a.b=b
b.a=a
del a
del b

# Test
