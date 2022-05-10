import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepali0e.append(weakref.ref(a,callback))
lst[0]=(a,a.c)
del keepali0e,lst,a
</code>
I am currently stuck to the starting point, and this is NOT a homework assignment.


A:

Your code does not actually crash.  It does produce a recursion depth error as you expect, but it does NOT crash.  I'm guessing that you are using some invalid memory debugging tool that detects you overflowing the stack, but it should not actually crash.
You can ignore the first <code>del</code> statement as it will only recurse once and won't do anything, but the next statement is the problem line:
<code>del lst[0]
</code>
A <code>__delitem__</code> call with a slice of length 1 is equivalent to a <code>__delitem__</code> on the actual item in the list.  There is no infinite recursion on a recursive datatype.  Consider this program:
<code>import weakref

class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
l
