import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepali0e.append(weakref.ref(a,callback))
lst.append(a)
del a
print(lst)

'''
'''
import weakref
from sys import getrefcount
class A(object):pass
a=A()
a.c=a
weakref.ref(a)
print(getrefcount(a))
'''
'''
import weakref
from sys import getrefcount
class A(object):pass
a=A()
a.c=a
ref=weakref.ref(a)
print(ref)
print(getrefcount(a))
'''
'''
import weakref
from sys import getrefcount
class A(object):pass
a=A()
a.c=a
ref=weakref.ref(a)
print(ref)
print(getrefcount(a))
'''
