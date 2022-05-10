import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
lst.append(weakref.ref(a.c,callback))
keepali0e.append(lst)
del a
while lst:
    print(lst)
    if not lst:
        lst.append(str())
</code>
The output is:
<code>['', &lt;weakref at 0x10b1f7b48; to 'A' at 0x10b1f7b00&gt;]
['', &lt;weakref at 0x10b1f7b48; to 'A' at 0x10b1f7b00&gt;]
['', &lt;weakref at 0x10b1f7b48; to 'A' at 0x10b1f7b00&gt;]
['', &lt;weakref at 0x10b1f7b48; to 'A' at 0x10b1f7b00&gt;]
['', &lt;weakref at 0x10b1f7b48; to 'A' at 0x10b1f7b00&gt;
