import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
# import gc
# gc.set_debug(gc.DEBUG_STATS|gc.DEBUG_LEAK)
a.keepalive=keepali0e
for i in range(100):
    a.c=a.c.c
    keepali0e.append(a.c)
    lst.append (lst[-1])
    keepali0e.append(str())
    lst.append (str())
    keepali0e.append(str())
    a.b=lst[0]
    print(i, len(gc.get_referrers(lst[0])), len(gc.get_referrers(('dummy', getattr(a, 'b')))))
    # print (gc.get_referrers(a))
