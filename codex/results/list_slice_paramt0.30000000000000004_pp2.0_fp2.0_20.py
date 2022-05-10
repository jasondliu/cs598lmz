import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepali0e.append(weakref.ref(a,callback))
del a
lst[0]
del keepali0e
lst[0]

#检查引用计数
import sys
a=[]
sys.getrefcount(a)
b=a
sys.getrefcount(a)
del b
sys.getrefcount(a)

#弱引用
import weakref
class A(object):pass
a=A()
r=weakref.ref(a)
r()
del a
r()

#弱引用的回调
import weakref
class A(object):pass
a=A()
r=weakref.ref(a,lambda x:print('dead'))
del a
r()

#弱引用的回调
import weakref
class A(object):pass
a=A()
r=weakref.ref(a,lambda x:print('dead'))
del a
r()

#弱引用的回调
import
