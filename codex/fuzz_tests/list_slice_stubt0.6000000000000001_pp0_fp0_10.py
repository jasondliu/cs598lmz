import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
a.d=a
keepalive.append(a)
keepalive.append(a.d)
keepalive.append(a.c)
del a
gc.collect()
if lst:
 print 'str not cleared'
else:
 print 'str cleared'
for i in range(2):
 keepalive.append(A())
del keepalive[0]
gc.collect()
if lst:
 print 'str not cleared'
else:
 print 'str cleared'
lst=[]
a=A()
a.c=a
a.d=a
keepalive.append(a)
keepalive.append(a.d)
keepalive.append(a.c)
del a
gc.collect()
if lst:
 print 'A not cleared'
else:
 print 'A cleared'
for i in range(2):
 keepalive.append(A())
del keepalive[0]
gc.collect()
if lst:
 print 'A not cleared'
else:
 print 'A cleared'
