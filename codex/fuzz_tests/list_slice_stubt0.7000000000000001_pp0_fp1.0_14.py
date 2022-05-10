import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
a.d=a
lst[0]=a
keepalive.append(lst[0])
print(len(lst),len(keepalive))
print(callback)
del a
del lst
print(len(keepalive))
print(keepalive)

lst=[]
class A(object):
    def __del__(self):
        print('del..')
        lst.append(1)
a=A()
a.b=a
del a
print(lst)

import gc
print(gc.garbage)
lst=[]
class A(object):
    def __del__(self):
        print('del..')
        lst.append(1)
a=A()
a.b=a
del a
print(lst)
print(gc.garbage)

import gc
print(gc.garbage)
lst=[]
class A(object):
    def __del__(self):
        print('del..')
        lst.append(1)
a=A()
