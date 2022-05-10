import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepali0e.append(weakref.ref(a.c,callback))
keepali0e.append(weakref.ref(a.c,callback))
del a
lst[0]
</code>
I expected to get an error because the callback should have deleted lst[0] but instead I get an empty string.
I also tried to put the callback in a class but it still doesn't work.
I am using python 2.7.6 on windows.
Thanks in advance


A:

The problem is that you are creating a hard reference to <code>a.c</code> when you do <code>a.c = a</code>.  This means that <code>a.c</code> will never be garbage collected.  If you add <code>del a.c</code> to your code, you'll see that the callback is called.

