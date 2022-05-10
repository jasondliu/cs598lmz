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


A:

When asking a question, please provide a minimal example of the behaviour you are seeing, rather than your entire codebase.
The answer to your question is that the <code>a.c=a</code> line creates a circular reference, which prevents the <code>a</code> object from being garbage collected.

