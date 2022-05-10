import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepalive.append(a)
w=weakref.ref(a,callback)
del a
print lst

'''

'''
#构造一个非循环的弱引用树
import weakref
class A(object):pass
def callback(x):print x
a=A()
b=A()
a.b=b
b.a=a
w=weakref.ref(a,callback)
del a
del b
'''


'''
import weakref
class A(object):pass
def callback(x):print "callback"
a=A()
b=A()
a.b=b
b.a=a
w=weakref.ref(a,callback)
del b
del a
'''

'''
class A(object):pass
def callback(x):print "callback"
a=A()
b=A()
a.b=b
b.a=a
w=weakref.ref(a,callback)
del a
del b

