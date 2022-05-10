import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepalive.append(a)
weakref.ref(a,callback)

#import gc
#gc.collect()
#print gc.garbage

#from weakref import WeakKeyDictionary
#class C(object):
#    def __init__(self):
#        self._data=WeakKeyDictionary()
#    def __set__(self,instance,value):
#        self._data[instance]=value
#    def __get__(self,instance,owner):
#        return self._data[instance]
#class D(object):
#    x=C()
#    def __init__(self,name):
#        self.name=name
#d=D('a')
#d.x=1
#print d.x
#del d
#print d.x

#import weakref
#class ExpensiveObject(object):
#    def __del__(self):
#        print '(Deleting %s)' % self
#obj=ExpensiveObject()
#r=weakref.ref(obj)
#print 'obj:
