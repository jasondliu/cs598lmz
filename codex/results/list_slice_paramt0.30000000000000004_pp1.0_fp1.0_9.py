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

#第二种引用
import weakref
class A(object):pass
def callback(x):print('callback')
a=A()
a.c=a
r=weakref.ref(a,callback)
print(r)
del a
print(r)

#第三种引用
import weakref
class A(object):pass
def callback(x):print('callback')
a=A()
a.c=a
r=weakref.ref(a,callback)
print(r)
a=None
print(r)

#第四种引用
import weakref
class A(object):pass
def callback(x):print('callback')
a=A()
a.c=a
r=weakref.ref(a,callback)
print(r)
a=None
print(r)
print(r())

#第五种引用
