import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepalive.append(a)
wr=weakref.ref(a,callback)
del a
print 'Before:'
print lst
print len(keepalive)

for i in range(0,10):
    if not lst:
        break
    print 'Iteration %s:' % i
    print lst
    print len(keepalive)
    print 'Keepalive 0 testable:'
    if keepalive[0].c:
        print keepalive[0].c
else:
    print 'Unable to complete loop, list not empty'
