import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a #cycle
callback(a)
keepali0e.append(callback)
del a
i=0
while lst:
    i+=1
