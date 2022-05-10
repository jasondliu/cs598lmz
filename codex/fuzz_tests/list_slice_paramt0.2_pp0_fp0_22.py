import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepali0e.append(weakref.ref(a,callback))
keepali0e.append(weakref.ref(a.c,callback))
del a
del keepali0e
gc.collect()
print(lst)

#['']

#删除回调函数
import weakref
class A(object):pass
def callback(x):print('callback called')
a=A()
a.c=a
keepali0e=weakref.ref(a,callback)
del a
gc.collect()
print(keepali0e)
keepali0e=None
gc.collect()

#callback called
#<weakref at 0x7f5b5f5d8f28; dead>

#删除回调函数
import weakref
class A(object):pass
def callback(x):print('callback called')
a=A()
a.c=a
keepali0e=weakref.ref(a,callback)
del a
gc.collect()
print(keepali0e)
keepali0e
