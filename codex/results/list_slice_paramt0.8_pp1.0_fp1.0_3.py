import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepali0e.append(weakref.ref(a.c,callback))
lst[0]="s"
del a
import gc
for i in range(2):
    gc.collect()
    time.sleep(0.2)
    if not lst:
        print "OK"
        break
else:
    print "NOT OK"
