import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
lst.append(a)
del a
keepalive.append(lst)
r=weakref.ref(lst,callback)
print(r)
del lst
print(r)
keepalive.pop()
</code>
Output:
<code>&lt;weakref at 0x015D27B8; to 'list' at 0x015D2740&gt;
None
</code>

