import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepali0e.append(weakref.ref(a))
keepali0e.append(weakref.ref(a.c))
keepali0e[0]().b=lst[0]
keepali0e[1]().b=lst[0]
del a
del a.c
gc.collect()
print lst
</code>
it output:
<code>['\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00']
</code>

