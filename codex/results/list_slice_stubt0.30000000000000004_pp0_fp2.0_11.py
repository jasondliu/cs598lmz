import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
lst.append(a)
del a
keepalive.append(lst)
gc.collect()
print lst
print len(gc.garbage)
del keepalive[:]
gc.collect()
print len(gc.garbage)
print gc.garbage

#测试弱引用
import weakref
class A(object):pass
a=A()
a.c=a
wr=weakref.ref(a,callback)
del a
print wr
print wr()

#测试弱引用
import weakref
class A(object):pass
a=A()
a.c=a
wr=weakref.ref(a,callback)
del a
print wr
print wr()

#测试弱引用
import weakref
class A(object):pass
a=A()
a.c=a
wr=weakref.ref(a,callback)
del a
print wr
print wr()

#测试弱引用
import weakref
