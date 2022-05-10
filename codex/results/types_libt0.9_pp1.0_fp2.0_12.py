import types
types.MethodType(lambda obj, name: getattr(obj, name), instance).__name__
</code>
<code>&gt;&gt;&gt; class A:
...     def __init__(self, name):
...         self.name = name
...     def get_name(self):
...         return self.name
...
&gt;&gt;&gt; instance = A('test')
&gt;&gt;&gt; getattr(instance, 'name')
'test'
&gt;&gt;&gt; instance.get_name()
'test'
&gt;&gt;&gt; getattr(instance, 'name')
'test'
&gt;&gt;&gt;
</code>

