import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepali0e.append(weakref.ref(a,callback))
print len(lst)
print a
print lst


import weakref
import gc
class ExpensiveObject(object):
    def __del__(self):
        print '(Deleting %s)'%self

obj=ExpensiveObject()
r=weakref.ref(obj)
print 'obj:',obj
print 'ref:',r
print 'r():',r()
print 'deleting obj'
del obj
print 'r():',r()
