import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepali0e.append(weakref.ref(a,callback))
del a,callback
print lst

a=A()
a.c=a
lst.append(a)
del a
print lst

print keepali0e

print "------------------"

import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepali0e.append(weakref.ref(a,callback))
del a,callback
print lst

a=A()
a.c=a
lst.append(a)
del a
print lst

print keepali0e

print "------------------"

# 方法：
# weakref.ref(object, callback=None)
# 创建一个weakref对象。当object被回收时，callback函数被调用。
# 参数：
#
