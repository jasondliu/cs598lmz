import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepali0e.append(weakref.ref(a,callback))
del a
print lst
print keepali0e

print
print
#测试弱引用指向的对象的弱引用列表
class A(object):pass
a=A()
b=A()
a.b=b
b.a=a
print a.b
print a.b.a
print b.a
print b.a.b
print a.__dict__
print b.__dict__
print weakref.getweakrefcount(a)
print weakref.getweakreflist(a)
print weakref.getweakrefcount(b)
print weakref.getweakreflist(b)
print weakref.getweakrefcount(a.b)
print weakref.getweakreflist(a.b)
print weakref.getweakrefcount(b.a)
print weakref.getweakreflist(b.a)

print
print
#测试弱引用指向的
