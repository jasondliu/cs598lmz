import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepali0e.append(weakref.ref(a.c,callback))
keepali0e
</code>
Output:
<code>[&lt;weakref at 0x7f8b4e4e4148; dead&gt;
</code>
And second:
<code>import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=A()
a.c.m=a.c
keepali0e.append(weakref.ref(a.c.m,callback))
keepali0e
</code>
Output:
<code>[&lt;weakref at 0x7f8b4dafe7c8; to 'A' at 0x7f8b4ea58330&gt;]
</code>
Full example:
<code>import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
def gc():
    for x in weakref.getweakrefs(keepali0e[0
