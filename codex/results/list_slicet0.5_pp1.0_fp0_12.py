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
I am using Python 3.2.2, and since the list is empty, I am getting a <code>IndexError</code> exception.
<code>Traceback (most recent call last):
  File "&lt;pyshell#15&gt;", line 1, in &lt;module&gt;
    while lst:keepali0e.append(lst[:])
IndexError: list index out of range
</code>
I am trying to make the weakref callback delete the first item in the list, and I am trying to make the while loop keep going until the list is empty.
How can I do this?


A:

You can't.  The <code>while</code> loop will execute the body before testing the condition.  The first time through, it will try to append an empty list to <code>keepali0e</code>.  The second time through, it will try to index into an empty list, and raise the <code>IndexError</code>.
You need to test the condition before executing the body:
<code>while lst:
    keepali0
