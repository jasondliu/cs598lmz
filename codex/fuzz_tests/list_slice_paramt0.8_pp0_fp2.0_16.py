import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepali0e.append(weakref.ref(a,callback))
del a
print lst

print '------------------------------'
import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=[a]
keepali0e.append(weakref.ref(a,callback))
del a
print lst

print '------------------------------'
import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=[a]
keepali0e.append(weakref.ref(a,callback))
del lst
print lst

print '------------------------------'
'''
析构函数
'''



import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=[a]
keepali0e.append(
