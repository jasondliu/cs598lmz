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
But this is not a real answer to my question.


A:

It looks like you are trying to make a list of all the cycles in your object graph.  You can do this by marking objects as you visit them.
<code>def find_cycles(obj):
    seen = set()
    def f(obj):
        if obj in seen:
            return [obj]
        seen.add(obj)
        if hasattr(obj, '__dict__'):
            for key,val in obj.__dict__.items():
                cycle = f(val)
                if cycle:
                    return [obj] + cycle
        return None
    return f(obj)
</code>
This will return <code>None</code> if no cycle was found, or a list of the objects in the cycle if it was.

