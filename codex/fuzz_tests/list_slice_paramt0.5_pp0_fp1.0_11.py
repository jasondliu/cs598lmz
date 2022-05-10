import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepali0e.append(weakref.ref(a,callback))
del a
del keepali0e
print lst
</code>
I expect the output to be <code>['&lt;weakref at 0x7f0a6e7f0c80; dead&gt;']</code> but the output is <code>[]</code>.


A:

This is a bug in Python 2.6.  It was fixed in Python 2.7.  See http://bugs.python.org/issue3136.

