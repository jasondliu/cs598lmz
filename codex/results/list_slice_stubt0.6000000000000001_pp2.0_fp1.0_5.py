import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepalive.append(a)
del a
weakref.ref(lst[0],callback)
</code>
In Python 2.6.5, this doesn't crash, but in Python 3.1.2, it does. I'm using Python 3.1.2 because I'm using Ubuntu 10.04 LTS (and Python 2.6.5 is the highest version in the repository).


A:

I don't know why your code crashes, but it's a bad idea to use <code>del</code> in a callback. The object being destroyed may be in the middle of a call to one of its methods (e.g. <code>__del__</code>), and that method may still be in the middle of accessing its instance variables. Accessing an instance variable on a destroyed object is undefined behavior.

