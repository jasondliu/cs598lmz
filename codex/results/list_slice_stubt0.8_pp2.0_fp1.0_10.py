import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
lst.append(a)
keepalive.append(lst)
del a
del lst
a=keepalive[0][1]
keepalive.clear()
b=a.c
del a
del b
s=str()
w=weakref.ref(s, callback)
print(w(), w())
</code>
When I run it, the address of w() changes.
<code>('', '0x0000000001CB3750')
</code>
The output I'm expecting is
<code>('', '0x0000000001CB3750')
</code>
I'm confused. Can anyone help? Thanks


A:

cython --embed
The reason you're getting the results you're getting is because the weakref is not being called when you're expecting it to be. You're using cython --embed to run your script, which means that the python interpreter is not in control of when it is being shut down. The only way you'll get your weakref callback to run before the python interpreter shuts down is if you manually call the garbage collector, like this:
<code>
