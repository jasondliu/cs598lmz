import types
types.MethodType(method, object)
</code>
What does <code>types.MethodType(method, object)</code> return?
I know that <code>method</code> is a function and <code>object</code> is a class instance. However, I am not sure what the return type is.
I tried to search online, but did not find anything.
Thanks.


A:

The return type is a <code>function</code>, with a <code>__self__</code> attribute pointing to the <code>object</code>.
I am not sure what the use case is for this, but here is how you can create a <code>method</code> type:
<code>&gt;&gt;&gt; class Foo(object):
...   def bar(self):
...     print(self)
... 
&gt;&gt;&gt; def baz(self):
...   print(self)
... 
&gt;&gt;&gt; f = Foo()
&gt;&gt;&gt; f.bar()
&lt;__main__.Foo
