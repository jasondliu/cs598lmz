import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepalive.append(a)
a=A()
a.c=a
lst.append(weakref.ref(a,callback))
lst[0]=lst[0]+lst[0]
"""
#===========================================================================

#===========================================================================
# 另一个例子：
#===========================================================================
"""
#===========================================================================
# 监听简单
#===========================================================================
import weakref
class A(object):pass
def callback(x):del lst[0]
lst=[str()]
a=A()
a.c=a
obj=weakref.ref(a,callback)
print obj
a.c=a
print obj
lst[0]=lst[0]+lst[0]
print obj
print obj.__str__()
print obj.__repr__()
print obj
print weakref.getweakrefcount(a)
print weakref.getweakrefs(a)
"""
#===========================================================================

import weakref
import sys

def callback
