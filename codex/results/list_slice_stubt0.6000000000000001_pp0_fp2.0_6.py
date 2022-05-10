import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepalive.append(a)
a.b=weakref.ref(a,callback)
print(keepalive)
print(lst)
del a

print(keepalive)
print(lst)

print('test7')

class A(object):pass
def callback(x):lst.append(True)
lst=[]
a=A()
a.c=a
weakref.ref(a,callback)
del a
print(lst)
print('test8')
del lst[:]
def callback(x):lst.append(True)
lst=[]
a=A()
a.c=a
weakref.ref(a,callback)
del a
print(lst)
print('test9')

class A(object):pass
def callback(x):lst.append(True)
lst=[]
a=A()
a.b=a
weakref.ref(a,callback)
del a
print(lst)
print('test10')

import weakref
class A(object):
