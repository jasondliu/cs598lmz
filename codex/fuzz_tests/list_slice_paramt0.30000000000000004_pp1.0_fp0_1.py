import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepali0e.append(weakref.ref(a,callback))
a=None
lst[0]

#计算对象的引用计数
import sys
a=[]
sys.getrefcount(a)
b=a
sys.getrefcount(a)
del a
sys.getrefcount(b)

#弱引用
import weakref
class A(object):pass
a=A()
r=weakref.ref(a)
r()
a=None
r()

#弱引用的回调函数
import weakref
class A(object):pass
a=A()
r=weakref.ref(a,lambda x:print('object has been deleted'))
a=None

#弱引用的清理
import weakref
class A(object):pass
a=A()
r=weakref.ref(a)
r()
r.__call__()
r.__call__()
r.__call__()
r.__call__
