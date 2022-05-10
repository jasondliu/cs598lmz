import types
types.MethodType(foo, None)
</code>
But it's not working for me.
What is the correct way to do it?


A:

You can do this using <code>types.FunctionType</code> and <code>types.MethodType</code>
<code>&gt;&gt;&gt; import types
&gt;&gt;&gt; def foo(self):
...     print "foo"
...
&gt;&gt;&gt; class A(object):
...     pass
...
&gt;&gt;&gt; A.foo = types.MethodType(types.FunctionType(foo.func_code, foo.func_globals, foo.func_name, foo.func_defaults, foo.func_closure), A)
&gt;&gt;&gt; A().foo()
foo
</code>

