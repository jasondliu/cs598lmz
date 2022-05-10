import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepalive.append(a)
wr=weakref.ref(a,callback)
</code>
In the interpreter, I can see that the number of objects increases by 3, while in my program, it increases by 5:
<code>&gt;&gt;&gt; import gc,sys
&gt;&gt;&gt; _=sys.gettotalrefcount()
&gt;&gt;&gt; a=A()
&gt;&gt;&gt; a.c=a
&gt;&gt;&gt; keepalive.append(a)
&gt;&gt;&gt; wr=weakref.ref(a,callback)
&gt;&gt;&gt; sys.gettotalrefcount()-_
3
&gt;&gt;&gt; del a
&gt;&gt;&gt; sys.gettotalrefcount()-_
0
</code>
What can I do to get the same behavior in my program as in the interpreter?


A:

You are using the wrong reference counting function.
<code>sys.get
