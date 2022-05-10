import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepali0e.append(weakref.ref(a,callback))
del a
lst[0]
del lst[0]
a=A()
keepali0e.append(weakref.ref(a))
a.c=A()
del a
keepali0e[0]()
del keepali0e
import weakref
def callback(x):print('callback')
def callback2(x):print('callback2')
class A(object):pass
a=A()
ref1=weakref.ref(a,callback)
ref2=weakref.ref(a,callback2)
print(ref1()is a)
print(ref2()is a)
del a
print(ref1()is None)
print(ref2()is None)
import weakref
class A(object):pass
a=A()
ref1=weakref.ref(a)
ref2=weakref.ref(a)
ref3=weakref.ref(a)
print(ref1()is a)
print(ref2()is a)
print(ref3()is a)
del a
print(ref1()is
