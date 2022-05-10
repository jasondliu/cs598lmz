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
</code>
This is the result:
<code>&gt;&gt;&gt; a.c=a
Traceback (most recent call last):
  File "&lt;pyshell#5&gt;", line 1, in &lt;module&gt;
    a.c=a
NameError: name 'a' is not defined
&gt;&gt;&gt; del a
&gt;&gt;&gt; while lst:keepali0e.append(lst[:])
&gt;&gt;&gt; 
&gt;&gt;&gt; 
</code>
<code>a</code> is not defined, but the list is still there.

