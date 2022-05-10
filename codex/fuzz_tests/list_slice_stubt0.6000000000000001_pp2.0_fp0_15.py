import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepalive.append(a)
del a
</code>
I am getting an assertion error at line <code>del a</code>
<code>AssertionError: 
</code>
Why am I getting this error?


A:

The assertion is triggered because there is a reference cycle. You have <code>a</code> referencing <code>a.c</code> and vice versa. <code>a</code> has a <code>__del__</code> method and <code>a.c</code> has a <code>weakref</code> on it.
When you delete <code>a</code>, it tries to invoke it's <code>__del__</code> method but the <code>weakref</code> is still alive, so it's not ready to be garbage collected. This is why you get the assertion.
See this link for more info:
http://docs.python.org/2/library/gc.html

