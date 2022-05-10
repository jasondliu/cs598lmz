import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepali0e.append(weakref.ref(a,callback))
del a
del keepali0e
import gc
for i in range(1000):
    gc.collect()
    print(lst)
import gc
class MyClass(object):
    def __del__(self):
        print('MyClass.__del__()')
obj=MyClass()
r=weakref.ref(obj)
print(r)
print(r())
del obj
print(r())
print(r)
import gc
gc.collect()
print(r)
gc.collect()
print(r)
import weakref
class Foo(object):
    def __init__(self,name):
        self.name=name
        self.bar=None
    def __repr__(self):
        return 'Foo({!r})'.format(self.name)
a=Foo('a')
b=Foo('b')
a.bar=b
b.bar=a
print(a)
print(b)
baz=weakref.ref(a)
print(baz)
print(b
