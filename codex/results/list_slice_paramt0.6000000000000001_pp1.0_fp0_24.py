import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepali0e.append(weakref.ref(a,callback))
keepali0e.append(weakref.ref(a))
del a
for i in range(10):
    gc.collect()
    print len(lst)
if len(lst)!=0:
    print "Cycle was not collected"
    sys.exit(1)
