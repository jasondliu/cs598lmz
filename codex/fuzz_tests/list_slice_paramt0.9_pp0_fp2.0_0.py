import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepali0e.append(weakref.ref(a.c,callback))
del lst,callback, A
import gc

for i in range(30):
    gc.collect()
    
print len(keepalive)


#有2个引用，

print a.c
