import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepali0e.append(a)
lst.append(a)
a.callback=callback
weakref.ref(a,a.callback)
print(lst)
del a
print(lst)
del lst
print(lst)
</code>
Output:
<code>['', &lt;__main__.A object at 0x00000000021129E8&gt;]
[&lt;__main__.A object at 0x00000000021129E8&gt;]
[&lt;__main__.A object at 0x00000000021129E8&gt;]
</code>

