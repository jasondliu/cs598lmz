import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
lst.append(weakref.ref(a))


lst[0]=str()
lst[0]=str()
gc.collect()
print lst
print len(gc.get_referrers(lst))
for r in gc.get_referrers(lst):
    print r.__class__,repr(r)
    if isinstance(r,dict):
        #print r.items()[0]
        print r.keys()[0]
print lst[1]().c

import threading
from collections import defaultdict
class Point(object):
    def __init__(self,*args):
        print self
        super(Point,self).__init__(*args)
        print 'Point init'
        #raise Exception("yiha!!!")
    #def __del__(self):print "Point",self
class Point1(Point):
    def __init__(self,*args):
        print self
        super(Point1,self).__init__(*args)
        #self.parent=self
        print 'Point
