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
</code>
how can i prevent del lst[0] this line executing?
and is there any other way to solve this issue?
<code>def callback(x):
    del lst[0]
    del keepali0e[:]
</code>
this is a solution. but i dont want to del keepali0e[:] this line executing.


A:

You can do this using pollute and unpollute.
<code>from guppy import hpy
h = hpy()

h.setref()
lst=['']

def callback(x):
    lst.pop()
    del lst[:]

keepali0e=[]
a=A()
a.c=a
keepali0e.append(weakref.ref(a,callback))

{*h.heap().setref()} - {*h.heap().getref()}
&gt;&gt; {'a': set([&lt;weakref at 0x000002E2A8A1BF30; to 'A' at 0x000002E2A
