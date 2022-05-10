import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
for i in xrange(1000000):
 if i==1000:
  lst.append(weakref.ref(a))
  a=None
 else:
  lst.append(keepali0e)
 lst[0]=A()
 lst[0].callback=callback
del keepali0e
lst[0].callback=(lst[0])
while len(lst):
 lst[0]=A()
del lst[0]
