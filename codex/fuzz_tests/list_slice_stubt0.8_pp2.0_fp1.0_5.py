import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
lst[0]=weakref.ref(a,callback)
keepalive.append(a)
del a
gc.collect()
del lst[:]
gc.collect()
#import gc;print(gc.collect())
#import gc;print(gc.collect())

lst=[]
lst.append(str())
lst[0]="a"
lst.append(str())
lst[1]="b"
lst.append(str())
lst[2]="c"
lst[2]=lst[1]
lst[1]=lst[0]
lst[0]=lst[2]
lst[2]=lst[1]
lst[1]=lst[0]
lst[0]=lst[2]
lst[2]=lst[1]
lst[1]=lst[0]
lst[0]=lst[2]
lst[2]=lst[1]
lst[1]=lst[0]
lst[0]=lst[2
