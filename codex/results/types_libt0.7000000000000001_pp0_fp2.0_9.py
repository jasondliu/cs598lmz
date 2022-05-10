import types
types.MethodType(mock_method, None, object)
</code>
but I get:
<code>TypeError: unbound method &lt;lambda&gt;() must be called with object instance as first argument (got nothing instead)
</code>
Is there a way to create a method object like the one I want?
I'm using Python 2.7.


A:

It should work if you pass the class as the first argument:
<code>types.MethodType(mock_method, object, object)
</code>

