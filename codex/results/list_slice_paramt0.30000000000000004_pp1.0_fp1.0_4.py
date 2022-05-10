import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepali0e.append(weakref.ref(a,callback))
print(lst)
del a
print(lst)

#第二种情况
import weakref
class A(object):pass
def callback(x):print('callback')
a=A()
a.c=a
keepali0e=weakref.ref(a,callback)
del a
print(keepali0e())

#第三种情况
import weakref
class A(object):pass
def callback(x):print('callback')
a=A()
a.c=a
keepali0e=weakref.ref(a,callback)
del a
print(keepali0e())

#第四种情况
import weakref
class A(object):pass
def callback(x):print('callback')
a=A()
a.c=a
keepali0e=weakref.ref(a,callback)
del a
print(keepali0e())

#第五种情况
import weakref
