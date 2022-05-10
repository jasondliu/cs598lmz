import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepalive.append(a)
lst.append(weakref.ref(a.c, callback))
del lst, a, keepalive
</code>
A. Следует корректно сделать удаление списка ссылок.
<code>import weakref
class A(object):pass
def callback(x):del lst[0]
keepalive=[]
lst=[str()]
a=A()
a.c=a
keepalive.append(a)
lst.append(weakref.ref(a.c, callback))
del lst[:], a, keepalive[:] # &lt;--- del lst[:]
</code>
Б. Следует корректно сделать собственно удаление элеме
