import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepali0e.append(weakref.ref(a,callback))
print "Should hace callback function."
a.c=str()
lst[0]="str"
a.c=lst[0]

del lst
import gc
gc.collect()
for i in range(1,100):
    keepalive=[]
    for j in range(1,20):
        l=[]
        for k in range(1,10):
            l.append(object())
        del l[5]
        del l[7]
        del l[2]
        keepalive.append(l)
        del l
    l=keepalive[0]
    del keepalive
    for x in range(100):
        if len(l) == 0:
            break
        l.append(object())
        del l[0]
    del l
    del keepalive
    gc.collect()
