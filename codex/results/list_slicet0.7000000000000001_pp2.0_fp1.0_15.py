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

The question is how to get rid of this error message, or at least how to get more information about the problem to know how to avoid it in the future.
I'm on Debian Linux 9.9, Python 2.7.13, and the code is executed in iPython (by the way, this problem does not exist in Python 3, but I need to stick with Python 2 for now).

I have tried to use gdb, but I can't see where the problem is.
I have tried to use <code>sys.getrefcount(a)</code> and <code>sys.getrefcount(a.c)</code> to see if I can find something that could help me, but it's too complex to find something.
I have tried to use the <code>gc</code> module to see if I can get more information on the problem.

I have read this page on the Python website, but it doesn't help me.
I have also tried to read the code of the <code>weakref</code> module, but it's a bit too complex for me, since I'm not that good in C.
Thank you.
