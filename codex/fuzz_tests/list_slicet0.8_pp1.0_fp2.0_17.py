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
If run this in Python 2.7, it will go into an infinite loop.
The problem is, <code>weakref.ref</code> is not a function which only receives one argument, but it is an object, which takes two arguments if not explicitly passed the second argument <code>callback</code>. So in this situation, <code>callback</code> is passed to <code>__init__</code> of the weak reference object. However, the callback is called even if the object is not collected. (And of course it will not be called if it is collected.)
In order to fix this, you should add a second line of code to <code>addKillable</code> and change <code>arg</code> to <code>(arg[0], arg[1])</code>. So that it looks like this:
<code>def addKillable(*arg):
   if len(arg) &gt; 1:
      arg = (arg[0], arg[1])
   k=Killable(*arg)
   lst.append(k)
   return k
</code>
And you should also change your third
