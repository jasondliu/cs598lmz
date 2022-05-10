import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepali0e.append(weakref.ref(a,callback))
keepali0e.append(weakref.ref(a.c,callback))
del a
gc.collect()
print lst
"""

"""
#7-4
#测试用例
class A(object):pass
def callback(x):
    print "callback"
    print x
a=A()
keepali0e=weakref.ref(a,callback)
print keepali0e
del a
gc.collect()
"""

"""
#7-3
#测试用例
class A(object):pass
def callback(x):
    print "callback"
    print x
a=A()
keepali0e=weakref.ref(a,callback)
print keepali0e
del a
gc.collect()
"""

"""
#7-2
#测试用例
class A(object):pass
def callback(x):
    print "callback"
    print x
a=A()
keepali0e=weakref.ref(a,callback)
