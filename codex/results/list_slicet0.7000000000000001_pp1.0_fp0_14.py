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


A:

When an object is deleted, the reference count of all the objects it refers to is decremented.  If it gets to zero, then they are deleted too.  If they have a <code>__del__</code> method, then it is executed.  This process continues recursively until every object that can be deleted has been deleted.  Here's an example:
<code>&gt;&gt;&gt; class Foo(object):
...     def __init__(self, msg):
...         self.msg = msg
...         print msg, 'created'
...     def __del__(self):
...         print self.msg, 'deleted'
...
&gt;&gt;&gt; class Bar(object):
...     def __init__(self, msg):
...         self.msg = msg
...         print msg, 'created'
...     def __del__(self):
...         raise Exception('I refuse to be deleted')
...
&gt;&gt;&gt; foo = Foo('foo')
foo created
&gt;&gt;&gt
