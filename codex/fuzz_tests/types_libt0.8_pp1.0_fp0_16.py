import types
types.ModuleType('foo')
# ...
</code>
How can I instantiate an abstract class?


A:

<code>types</code> has no public API for instantiating arbitrary classes. You could use the fact that <code>ModuleType</code> is a subclass of <code>type</code>, but that's a hack that could break any time. If you really do need to do this, then <code>abc</code> provides the hooks you need:
<code>abc.ABCMeta.__new__(abc.ABCMeta, 'Foo', (object,), {'__module__': 'foo'})
</code>

