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
I get this output (after a long pause):
<code>[]
[]
</code>
but on the second run, I get this output:
<code>[]
[]
[]
[]
[]
[]
[]
...
</code>
I'm running Python 2.7.3 on Ubuntu 12.04.
Why does this happen and how can I fix it?

