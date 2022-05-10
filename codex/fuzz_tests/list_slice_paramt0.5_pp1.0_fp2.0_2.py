import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepali0e.append(weakref.ref(a,callback))
del a
print len(lst)

#output:0
#reason:
#1.create a object a
#2.a.c=a,so a has a reference to itself
#3.a.b=callback,so when a is deleted,callback will be called
#4.del a,a's reference count is 0,but it still has a reference to itself,so it will not be deleted
#5.a.b is called,so a.c=a is removed,and a's reference count is 0,so a is deleted
#6.the reference count of lst[0] is 0,so lst[0] is deleted

#question 2
import weakref
class A(object):pass
def callback(x):del lst[0]
keepalive=[]
lst=[str()]
a=A()
a.c=a
keepalive.append(weakref.ref(a,callback))
a.d=callback
del a
print len(lst)

#output:1
#reason:
#1.create a object a
