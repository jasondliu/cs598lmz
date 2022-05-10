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
print keepali0e
</code>
I am trying to understand the output of this code. I am not able to understand why the output is <code>[[&lt;weakref at 0x7f6c9d6b9b90; to 'A' at 0x7f6c9d6b9c50&gt;], []]</code>.
I am not able to understand why the second element of the list is empty.

