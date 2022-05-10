import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepali0e.append(weakref.ref(a,callback))
keepali0e.append(weakref.ref(a.c,callback))
print a,a.c
a=None
print lst
# output:
# <__main__.A object at 0x7f08a4a85f90> <__main__.A object at 0x7f08a4a85f90>
# ['\x00\x00\x00\x00\x00\x00\x00\x00']

### 弱引用可以作为字典的键值
class A(object):pass
d=weakref.WeakKeyDictionary()
a=A()
d[a]=1
print d[a]
del a
print d
# output:
# 1
# {}

### 无参数的弱引用与普通引用相同
import weakref
class A(object):pass
a=A()
b=a
c=weakref.ref(a)
print
