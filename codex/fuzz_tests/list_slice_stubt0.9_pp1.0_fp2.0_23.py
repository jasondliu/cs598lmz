import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
a.d=a.c
keepalive.append(a.d)
lst.append(a)
lst.append(a.d)
lst.append(a.c)
lst.append(a.d)
weakref.ref(a,callback)
</code>
It works on Python 2.6 and Python 2.7. 
This problem is similar to issue 3291.

