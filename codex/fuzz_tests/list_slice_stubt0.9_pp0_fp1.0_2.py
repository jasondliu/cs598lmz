import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
a.wref=weakref.ref(a,callback)
print(lst)
del a.c
del a.wref
print(lst)
del a
print(lst)
import gc
print(gc.get_referrers(keepalive))
o=keepalive[:]
del keepalive
print(gc.get_referrers(o))
del o
print(gc.get_referrers(str()))


import gc
l=[i for i in range(50)]

for i in range(10):
 l.append((str(),str(),str(),str(),str(),str(),str(),str(),str(),str(),str(),str(),str(),str(),str(),str()))
 print(gc.collect())

l=l*100
print(gc.collect())


import gc
import sys
class A:
  def __del__(self):
    print('del:',self.__class__.__name__)
    sys.stdout.flush()
a=A()
b=A()
a.b=
