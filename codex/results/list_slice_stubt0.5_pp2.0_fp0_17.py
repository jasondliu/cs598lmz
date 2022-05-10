import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepalive.append(a)
lst.append(weakref.ref(a.c,callback))
del a
print lst
print keepalive
</code>
The output is:
<code>['', &lt;weakref at 0x7f9b5a5b7e78; to 'A' at 0x7f9b5a5b7f60&gt;]
[&lt;__main__.A object at 0x7f9b5a5b7f60&gt;]
</code>
As you can see, the item in the list is not deleted.
If you change the line
<code>a.c=a
</code>
to
<code>a.c=None
</code>
you will see that the item in the list is deleted.
My question is:
Why is the item in the list not deleted?


A:

<code>a</code> is alive and references <code>a.c</code>, which is <code>a</code> itself. So <code>a</code> is reachable and
