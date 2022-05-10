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
print(keepali0e)
</code>
In Python 3.7.1, I get a <code>RecursionError: maximum recursion depth exceeded</code> error.
I am using a similar code to the above to check for cycles in a graph. The graph is represented as a dictionary.
I was wondering if there is a way to do this without the <code>RecursionError</code>?


A:

Python 3.4 introduced a new <code>weakref.finalize</code> class that allows you to register a callback for any object, regardless of whether it is referenced or not.
<code>import weakref

class A(object):pass

def callback(x):
    print("A was deleted")

keepali0e = []
lst = [str()]
a = A()
a.c = a
weakref.finalize(a, callback)
del a
while lst:
    keepali0e.append(lst[:])
print(keepali0e)
</code>

