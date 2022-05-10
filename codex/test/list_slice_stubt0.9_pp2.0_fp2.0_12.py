import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a.b=a.a=callback
i=0
while i<1000:a.c=a.b=a.a=a;i+=1
while i<10000:a.c=a.b=a.a;i+=1
a.c=a.b=a.a=keepali0e
a.c=a.b=a.a=a
a.c=a.b=a.a=callback
del a.c,a.b
while a.a:pass
del a.a
gc.collect()
