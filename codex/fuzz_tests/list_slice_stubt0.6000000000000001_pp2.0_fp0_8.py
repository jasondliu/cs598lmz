import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
a.b=a
a.a=a
keepalive=[]
for i in range(1,200):
    a=A()
    a.a=a
    a.b=a
    a.c=a
    w=weakref.ref(a,callback)
    keepalive.append(a)
    keepalive.append(w)
    keepalive.append(w)
    del a
del keepalive
gc.collect()
print len(lst)
</code>
My question is:
Why does this code print <code>1</code>? I didn't expect that.
I thought that <code>lst[0]</code> is the only object in the list, but in my opinion, it should be removed by the garbage collector, because it is not referenced.
Can anyone explain this behaviour?


A:

Your code is equivalent to:
<code>&gt;&gt;&gt; class A(object):pass
&gt;&gt;&gt; def callback(x):del lst[0]
&gt;&
