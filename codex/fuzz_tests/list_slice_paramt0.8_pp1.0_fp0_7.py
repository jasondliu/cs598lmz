import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepali0e.append(weakref.ref(a,callback))
a.c=1
print(a.c)
print(lst[0])
</code>
It seems the garbage collector doesn’t activate. If I add <code>print(gc.collect())</code> it prints <code>0</code>, so why the cyclic reference hasn’t been cleared?


A:

It seems this was an issue with the reference being from an old object to a new object. If I modify the code like this:
<code>class A(object): pass
def callback(x): del lst[0]

lst = [str()]
a = A()
# Add this line     
b = A() 
a.c = b
keepali0e.append(weakref.ref(a, callback))
a.c = 1
print(a.c)
print(lst[0])
</code>
Then it works.

