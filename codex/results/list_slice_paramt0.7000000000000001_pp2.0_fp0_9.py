import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepali0e.append(weakref.ref(a,callback))
del a
gc.collect()
print len(lst)

"""
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepali0e.append(weakref.ref(a,callback))
print len(lst)
del a
gc.collect()
print len(lst)
"""

"""
#weakref.ref(x,[callback])
#x:object,callback:function
lst=[str()]
def callback(x):del lst[0]
keepali0e=[]
keepali0e.append(weakref.ref(lst[0],callback))
del lst[0]
print len(lst)
gc.collect()
print len(lst)
"""

"""
#weakref.proxy(x,[callback])
#x:object,callback:function
lst=[str()]
def callback(x):del lst[0]
keepali0e=[]
b
