import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
b=A()
b.c=a
A.d=property(lambda self:self.c)
A.e=property(lambda self:a.c)
keepalive=weakref.ref(b,callback)
lst*=30000000000005
</code>
Or does it depend on the python implementation, eg. CPython?


A:

The CPython interpreter doesn't have infinite precision.  It uses C-sized integers for its internal counting, which means that on 32-bit systems, you can only count up to about 2 billion, and on 64-bit systems you can only count up to about 2 billion billion.
That can vary by implementation, of course.  If you're using a language that tries to emulate Python, the first thing to check is the implementation -- the specifics of the implementation could make a big difference.  For example, even an implementation like Jython would probably have different limits because it uses Java-sized integers instead of C-sized integers.

As an example of how the implementation may affect things, note that both Python 3 and 2 versions of your code fail with a different exception on 32-bit vs. 64-bit
