import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
weaklist=[a]
weaklist.append(weakref.ref(callback,lst))
del keepalive
lst

#Test for __getitem__ not returning an int
class X(object):
     def __getitem__(self, index):
          return "", None
import weakref
y=X()[:]
if heaplength()!=0: raise Exception, "Heap is not empty"

#Test for finalizers which live in the heap
def nop(x):pass
class X(object):pass
x=X()
import sys
weaklist=[]
for i in xrange(100):
    try:
        weaklist.append(weakref.ref(sys.maxint,None))
    except OverflowError:
        import gc
        gc.collect()
        print "passed"
        break

#Test for __getitem__ doing an arbitrary number of calls
class X(object):
     nodes={}
     def __getitem__(self,index):
          while 1:
               try: return self.nodes[index]
