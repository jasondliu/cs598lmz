import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepali0e.append(weakref.ref(a,callback))
del a
while lst:keepali0e.append(lst[:])
print len(keepali0e)
</code>
It will crash in 16 hours on my PC.
I think this is because the ref callback function cannot delete reference from list, so the <code>a.c=a</code> makes a cycle of weak reference.
Is it right?


A:

<code>  1. while lst:
  2.     keepali0e.append(lst[:])
  3. 
  4. print len(keepali0e)
</code>
This is an infinite loop.

