import types
types.ModuleType
</code>
<code>&gt;&gt;&gt; types.ModuleType
&lt;type 'module'&gt;
</code>
It shows that <code>types.ModuleType</code> is a class, so I can create an instance of it by a constructor, but when I try to call it, I get this error:
<code>&gt;&gt;&gt; types.ModuleType()
Traceback (most recent call last):
  File "&lt;stdin&gt;", line 1, in &lt;module&gt;
TypeError: required argument 'name' (pos 1) not found
</code>
It has a <code>name</code> argument, so I supplied it
<code>&gt;&gt;&gt; types.ModuleType('test')
&lt;module 'test' (built-in)&gt;
</code>
It works, but I'm confused, where is <code>test</code>?
<code>&gt;&gt;&gt; test
Traceback (most recent call last):
  File
