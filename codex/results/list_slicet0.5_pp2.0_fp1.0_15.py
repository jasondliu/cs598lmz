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
print len(keepali0e)
</code>
This code is taken from http://www.python.org/dev/peps/pep-0435/.
This code is not working in python 3.2 and 3.3, but is working in python 2.7.
Is there a way to make this code work in python 3.3?


A:

<code>lst=[str()]
</code>
You can't create a weakref to an empty string.  <code>str()</code> is an immutable object.  You can create a weakref to a mutable object, but not to an immutable object.  If you change the above line to
<code>lst=[[]];
</code>
then your code will work in Python 3.3.

