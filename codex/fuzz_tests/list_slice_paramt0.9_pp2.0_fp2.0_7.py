import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepali0e.append(weakref.ref(a,callback))
</code>
This code is supposed to delete an item from the list lst when the object a gets deleted. The code I wrote gets these errors:
<code>    a.c=a
TypeError: 'str' object does not support item assignment

lst=[str()]
TypeError: 'str' object is not callable
</code>
Please could someone explain why these errors happen and show me the right way to make an object and a string weakreference?
I want to be able to dereference the weakreference before it gets deleted.


A:

It looks like you're using IronPython.  There are two ways to create a string object in IronPython.  The <code>str()</code> function creates an empty string.  The string class is the <code>str</code> type.
I'm guessing the reason that you are getting these errors is that you are trying to create a string object, then redefine the <code>str</code> constant, which is not allowed.  

