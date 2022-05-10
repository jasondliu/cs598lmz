import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepali0e.append(a)
del a
lst.append(a)
del lst
print(gc.collect())

#删除引用循环
import weakref
class A(object):pass
def callback(x):print('callback')
lst=[str()]
a=A()
a.c=a
lst.append(a)
del a
lst.append(a)
del lst
print(gc.collect())

#弱引用
import weakref
class A(object):pass
def callback(x):print('callback')
lst=[str()]
a=A()
a.c=a
lst.append(a)
del a
print(gc.collect())
lst.append(a)
del lst
print(gc.collect())

#弱引用
import weakref
class A(object):pass
def callback(x):print('callback')
lst=[str()]
a=A()
a.c=a
lst.
