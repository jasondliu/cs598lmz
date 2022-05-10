import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepalive.append(a)
a.b=weakref.ref(a,callback)
gc.collect()
print lst
</code>
I run this code in python 2.7.3 and get the following result:
<code>['', '', '', '']
</code>
But in python3.3.0, it will print:
<code>['', '', '']
</code>
It seems that the cyclic reference is not collected.
So, is it a bug in python3.3.0?

