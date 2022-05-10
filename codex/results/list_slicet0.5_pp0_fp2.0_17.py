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
del keepali0e
</code>
The code is simple:
1. Create a class A with a circular reference to itself.
2. Create a list lst with one element.
3. Create an instance a of A and assign a.c to a.
4. Register a weak reference of a to lst with callback function.
5. Delete a.
6. Now, the circular reference is broken and the callback function is called. The element in lst is deleted.
7. Keep appending lst to keepali0e.
8. Delete keepali0e.
The code runs fine with Python 2.7. But I get MemoryError with Python 3.4.1.
The code is from my answer to a question on Stack Overflow. I think it's a bug in Python 3.4.1.
I'm using Windows 7 64-bit.


A:

It looks like a bug in Python 3.4.1.
I've just tried the following code in Python 2.7.6 and Python 3.4.1:
<code>import weakref

class A(
