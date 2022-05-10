import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepali0e.append(weakref.ref(a,callback))
del a
while lst:keepali0e.append(lst[:])
print 'DONE'
# creates a reference cycle

#import sys
#def f():return 3
#setattr(sys,'x',1)
#print sys.x
#print dir(sys)
#print sys.__dict__['x']
#sys.__dict__['x']=f
#print sys.__dict__
#print sys.x()
#print type(f)
#print type(sys.x)
#
import sys as ss
class A(object):
    def __new__(cls):
        cls.y =  cls
        return super(A,cls).__new__(cls)
    def __getattr__(self,attr):
        print 'no attribute',attr
        return 2
    def f(self,attr):
        print attr
        return 1
    def __setattr__(self,attr,thing):
        print 'get it!'
        self.__dict__[attr] = thing
    def __delattr__(self,attr):
        print 'get it'
a=A()
print a.
