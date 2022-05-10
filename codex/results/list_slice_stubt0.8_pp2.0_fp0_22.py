import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a.b=a.a=0
keepalive.append(a)
aa=weakref.ref(a,callback)
assert lst==[str()],lst
del a
for i in range(10):
    gc.collect()
assert lst==[],lst
class A(object):pass
a=A()
b=A()
a.b=b
b.a=a
keepalive.append(a)
keepalive.append(b)
wr = weakref.ref(a)
assert wr() is a
del b
gc.collect()
assert wr() is a
wr = weakref.ref(b)
assert wr() is None
wr = weakref.ref(a)
assert wr() is None
del a
class A(object):
    def __del__(self):
        self.x = 42
a = A()
wr = weakref.ref(a)
assert wr() is a
assert a.x == 42
a = None
a = A()
wr = weakref.ref(a)
assert wr() is a

