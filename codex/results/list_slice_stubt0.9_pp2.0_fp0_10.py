import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
weakref.proxy(a,callback)
lst.pop()
keepalive.append(a)
print(a.__class__)

#垃圾收集实现
class Graph:
    def __init__(self,name):
        self.name=name
        self.next =None
    def set_next(self,next):
        print('%s.next=%s' % (self,next))
        self.next=next
    def __repr__(self):
        return '%s(%s)' % (self.__class__.__self__,self.name)
one =Graph('one')
two = Graph('two')
one.set_next(two)

import gc
found_objects=gc.get_objects()
print('%d object before' % len(found_objects))

x=1
import sys
print('%d refeence ' % sys.getrefcount(x))
print('%d object after ' % len(found_objects))
