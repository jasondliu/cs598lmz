import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepali0e.append(weakref.ref(a,callback))
lst.append(a)
del a
del keepali0e
print lst
</code>
I am trying to understand the above code.
I have run it in python 2.7.8 and it gives me the following output:
<code>['', &lt;__main__.A object at 0x037C3F70&gt;]
</code>
I have run it in python 3.4.3 and it gives me the following output:
<code>['', &lt;__main__.A object at 0x00000000037C3F70&gt;]
</code>
I am trying to understand the above code.
I have read the following article:
http://www.doughellmann.com/PyMOTW/weakref/
I have read the following article:
https://docs.python.org/2/library/weakref.html
I have read the following article:
https://docs.python.org/3/library/weakref.html
I have read the following article:
http://code.activestate.com/recipes/812
