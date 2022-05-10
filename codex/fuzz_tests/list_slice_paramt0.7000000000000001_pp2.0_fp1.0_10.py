import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepali0e.append(weakref.ref(a,callback))
</code>
I am trying to make a circular reference and make the object a garbage. But it is not happening. I have tried with a list object also.

