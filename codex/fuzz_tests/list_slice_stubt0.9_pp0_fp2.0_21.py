import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
for i in xrange(1000):
try:keepalive=weakref.ref(a)
except:pass
del a
a=A()
a.c=a
keepali0e.append(keepalive)
lst.append(None)
del a
for i in xrange(10):
try:l=len(lst)
except:l= -1
if l!=1000:print l
for i in xrange(1000):
a=A()
a.c=a
lst[i]=a
for i in xrange(100):
r=lst[999]
r.c=r
try:l=len(lst)
except:l= -1
if l!=1000:print l
