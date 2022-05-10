import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepalive.append(a)
del a
gc.collect()
print lst
</code>
I'm trying to understand how this code works. I know that the list is empty after the callback function is called. I'm not sure why this happens. 

