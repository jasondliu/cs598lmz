import types
types.new_class('Foo')
</code>
This works in Python 2.7 but doesn't work in Python 3.4. Why doesn't it work in Python 3.4? Is there any alternative?


A:

The <code>types</code> module is not part of the public API.  The <code>types</code> module was meant for internal use.
The <code>types</code> module has been deprecated in Python 3.  You will have to use <code>type</code> to create a new class.
<code>Foo = type('Foo', (object,), {})
</code>

