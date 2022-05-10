import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepali0e.append(weakref.ref(a,callback))
del a
print len(lst)
</code>
Edited:
I want <code>lst</code> to be empty when the program runs, but it still outputs 1. If I run the program again and again, sometimes the output is 1 and sometimes the output is 0. I don't know when it will be 0, can anyone tell why it becomes 0 sometimes?
Edited:
Here is another one:
<code>import weakref,gc
class A(object):pass
def callback(x):del lst[0]
a=A()
a.c=a
lst=[str()]
keepalitre.append(weakref.ref(a,callback))
del a
print len(lst)
</code>
It also sometimes gives me 0 and sometimes 1, why?
But if I do like this, the output will always be 1:
<code>import weakref,gc
class A(object):pass
def callback(x):del lst[0]
lst=[str()]
a=A()
a.c=a
keepali0e.append(weak
