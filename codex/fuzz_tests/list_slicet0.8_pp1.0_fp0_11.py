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
内存泄漏的一个例子
import weakref
class A(object):pass
def callback(x):print('callback')
a=A()
a.c=a
keepali0e=weakref.ref(a,callback)
del a
gc.collect()
print('done')
'''
