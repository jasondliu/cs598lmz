import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepali0e.append(weakref.ref(a,callback))
lst[0]='a'
print(a)
del a
print(lst)
print(keepali0e)
print(keepali0e[0]())
print(lst)

#单个对象弱引用
import weakref
class A(object):pass
def callback(x):print('callback')
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepali0e.append(weakref.ref(a,callback))
print(a)
del a
print(keepali0e[0]())

#单个对象弱引用
import weakref
class A(object):pass
def callback(x):print('callback')
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepali0e.append(weakref.ref(a,callback))
print(a)
del a
print(keepali0e[0]())

#
