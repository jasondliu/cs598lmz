import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepali0e.append(weakref.ref(a,callback))
lst[0]=a
print len(keepali0e)
print len(keepali0e)
"""
"""
import weakref
class A(object):
    def foo(self,x,y):
        print 'calling foo with ',x,y
class B(object):
    def bar(self,a,b):
        print 'calling bar with ',a,b
def callback(x):
    print 'callback for',x
    del lst[0]


lst=[A()]
keepali0e=[A(),B()]
keepali0e[0].foo=weakref.ref(keepali0e[1].bar,callback)
keepali0e[0].foo(1,'2')
print len(keepali0e)
lst[0].foo(3,'4')
pri
