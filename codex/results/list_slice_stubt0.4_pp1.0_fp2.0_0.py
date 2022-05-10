import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepalive.append(a)
del a
lst[0]=lst
del lst
import gc
gc.collect()
print len(keepalive)
</code>
I get <code>2</code> as answer.
2)
<code>import weakref
class A(object):pass
def callback(x):del lst[0]
keepalive=[]
lst=[str()]
a=A()
a.c=a
keepalive.append(a)
del a
lst[0]=lst
del lst
import gc
gc.collect()
print len(keepalive)
</code>
I get <code>1</code> as answer.
So, my question is:
Why in the first case I get 2 as answer, while in the second case I get 1 as answer?

