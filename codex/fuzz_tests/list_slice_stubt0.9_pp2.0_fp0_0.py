import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
a.d=a
print A.__hash__(a)
print a
w=weakref.ref(a,callback)
print w
import os
print os.getcwd()
print w.add_child("w1")
print w.add_child("w2")
print w.del_child("w1")
print w.add_child("w1")
print w.get_child("w1")
