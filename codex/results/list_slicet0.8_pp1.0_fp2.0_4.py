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
print len(keepali0e)
"""

"""
#测试循环引用导致执行了callback（因为lst被删除了）
import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepali0e.append(weakref.ref(a,callback))
del a
del lst[0]
while lst:keepali0e.append(lst[:])
print len(keepali0e)
"""

"""
#测试循环引用导致执行了callback（因为lst被删除了）
import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
