import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
a.b=a
a.a=a
a.d=lst
a.e=callback
keepali0e.append(a)
del a
del keepali0e
del lst
gc.collect()
</code>
In the interactive interpreter, this segfaults. In a python script, it does not. Also, it does not segfault with:
<code>del lst[0]
</code>
or
<code>a.e=lambda x:x
</code>
I'm using Python 2.6.4 on Ubuntu 10.04.
This does not segfault with Python 2.5.2 on Ubuntu 8.04.
I'm also not entirely sure if this is a bug or if I'm doing something that I'm not supposed to be doing.

