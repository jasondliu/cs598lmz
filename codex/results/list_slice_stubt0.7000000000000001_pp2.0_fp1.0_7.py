import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
def f(n, lst):
    if (n==0):
        return
    lst.append(a)
    f(n-1, lst)
    lst.pop()
    lst.append(a)
    lst.pop()
f(1000000, lst)
for n in range(1):
    lst.append(a)
    keepalive.append(lst)
del a
lst[0]
</code>
This is a sample code and I found an interesting result in pypy.
The code is very simple:

create an object A and a cycle reference a.c=a
create a list lst and append a
pop a and append a again
delete a
and then exit

The result is:

In python3.3, it exits normally
In pypy3.3, it raises AssertionError: list modified during iteration

Why is this happening?
I noticed that there is a <code>gc.collect()</code> in pypy3.3's list.c:
<code>PyObject **
