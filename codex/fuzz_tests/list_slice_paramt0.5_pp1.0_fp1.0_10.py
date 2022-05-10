import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepali0e.append(weakref.ref(a,callback))
del a

#可以看到，当del a的时候，会调用callback方法，结果是lst中的第一个元素被删除了

#可以使用weakref.WeakKeyDictionary类来跟踪对象的弱引用，可以在对象不再使用的时候删除它们：

import weakref
class A(object):pass
d=weakref.WeakKeyDictionary()
a=A()
d[a]=1
print(d)
del a
print(d)
