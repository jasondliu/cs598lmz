import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
lst[0]=lst
keepalive=[a]
p=weakref.ref(a,callback)
a.c=a.c

"""
"""
class A(object):pass
def callback(x):del lst[0]
keepalive=[]
lst=[]
a=A()
a.c=a
lst.append(lst)
keepalive=[a]
p=weakref.ref(a,callback)
a.c=a.c
"""
"""
class A(object):pass

def callback(l):del lst[0]
keepalive=[]
lst=[]
a=A()
lst.append(lst)
keepalive=[a]
p=weakref.ref(a,callback)
a.c=a.c
"""
"""
import weakref
class A(object):pass
lst=[]
keepalive=[]
def callback(x):del lst[0]
a=A()
lst.append(lst)
keepalive=[a]
p=
