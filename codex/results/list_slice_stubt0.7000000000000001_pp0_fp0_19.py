import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
lst.append(a)
keepalive.append(lst)
del a
lst=weakref.WeakSet(lst,callback)
del keepalive[:]
try:
    del lst
except ReferenceError:pass
else:print('1')
def callback(x):del lst[1]
keepalive=[]
lst=[str()]
a=A()
a.c=a
lst.append(a)
keepalive.append(lst)
del a
lst=weakref.WeakSet(lst,callback)
del keepalive[:]
try:
    del lst
except ReferenceError:pass
else:print('2')
def callback(x):del lst[0]
keepalive=[]
lst=[str()]
a=A()
a.c=a
lst.append(a)
keepalive.append(lst)
del a
lst=weakref.WeakSet(lst,callback)
del keepalive[:]
try:
    del lst
except ReferenceError
