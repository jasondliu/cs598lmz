import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepali0e.append(weakref.ref(a,callback))
del a
lst

#调用回调函数
import weakref
class A(object):pass
def callback(x):print 'callback'
lst=[A()]
a=A()
a.c=a
lst.append(weakref.ref(a,callback))
del a
lst
lst[1]()
lst[1]()
lst[1]()
del lst

#引用计数
import weakref
class A(object):pass
def callback(x):print 'callback'
lst=[A()]
a=A()
a.c=a
lst.append(weakref.ref(a,callback))
del a
lst
lst[1]()
lst[1]()
lst[1]()
del lst

#引用计数
import weakref
class A(object):pass
def callback(x):print 'callback'
lst=[A()]
a=A()

