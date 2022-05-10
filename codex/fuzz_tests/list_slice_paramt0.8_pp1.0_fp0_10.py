import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepali0e.append(weakref.ref(a,callback))
a=None
print keepali0e
print lst
del lst
print keepali0e
'''

'''
import weakref
class A(object):pass
def callback(x):print x
a=A()
a.c=a
keepali0e=weakref.ref(a,callback)
a=None
'''

'''
import gc
class A(object):pass
def callback(x):print x
a=A()
a.c=a
keepali0e=weakref.ref(a,callback)
a=None
'''

'''
import weakref
class A(object):pass
def callback(x):print x
a=A()
a.c=a
keepali0e=weakref.ref(a,callback)
a=None
'''

'''
import weakref
class A(object):pass
def callback(x):print x
a=A()
a.c=a
keepali0e=weakref.ref(a,callback)
a=None
'''
