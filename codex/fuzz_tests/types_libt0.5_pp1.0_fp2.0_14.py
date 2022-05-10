import types
types.new_class("MyClass", (object,), {})
</code>
The documentation states the following:
<blockquote>
<p>The third argument is a dictionary containing initial values for the
  class’s namespace; this should be a dictionary as returned by
  vars().</p>
</blockquote>
But when I try to pass a dictionary as the third argument, I get the following error:
<code>TypeError: vars() argument must have __dict__ attribute
</code>
What am I doing wrong?


A:

You should pass an object, not a dictionary:
<code>&gt;&gt;&gt; class MyClass(object):
...     pass
... 
&gt;&gt;&gt; types.new_class("MyClass", (object,), MyClass)
&lt;class 'MyClass'&gt;
</code>

