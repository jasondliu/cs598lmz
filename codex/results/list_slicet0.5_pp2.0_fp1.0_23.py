import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepali0e.append(weakref.ref(a,callback))
del a
while lst:keepali0e.append(lst[:])

#第二个
import gc,weakref
class A(object):pass
def callback(x):print('callback')
a=A()
a.c=a
keepali0e=weakref.ref(a,callback)
del a
gc.collect()

"""
weakref.ref(obj[,callback])
callback是一个可选的回调函数，如果指定了callback，当引用对象被回收时，该回调函数会被调用。
"""

#第三个
import weakref
class A(object):pass
def callback(x):print('callback')
a=A()
a.c=a
keepali0e=weakref.ref(a,callback)
del a
print(keepali0e)
print(keepali0e())

#第四个

