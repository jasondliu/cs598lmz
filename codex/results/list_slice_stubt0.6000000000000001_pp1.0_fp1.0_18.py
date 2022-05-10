import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepalive.append(a)
del a
for i in lst:
    keepalive.append(weakref.ref(i,callback))
</code>
When I was testing this code, I found that the callback would not be called.
I want to know why and how to fix it.


A:

The callback is called, but not when you think it is.
The <code>del lst[0]</code> statement is executed when the loop exits. The weakref is cleared only if the variable is still in scope. Since the variable is cleared as part of the loop, the weakref is not cleared.
You could use a flag to tell the loop to exit, or you could use <code>itertools.takewhile()</code> to limit the loop to the length of the original list:
<code>from itertools import takewhile

for i in takewhile(lambda _: lst, lst):
    keepalive.append(weakref.ref(i,callback))
</code>

