import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a #self-reference
keepalive=a
b=[a,lst]
c=[lst,b]
del a
del b
del lst
gc.collect()
lst=weakref.WeakList(c,callback)
del c
gc.collect()
</code>
You could of course convert the WeakList to a list, then add the string to lst, just make sure to always take the last element from weaklist, as the middle elements may have already been deleted by the callback. 

