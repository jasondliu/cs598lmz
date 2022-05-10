import types
types.MethodType(c.x, None, c)
</code>
But what's the difference between the two examples?


A:

<code>types.MethodType(c.x, None, c)</code> fails because <code>c.x</code> is already a method. You can't use <code>MethodType</code> to add a method on a bound method.
<code>c.x = types.MethodType(c.x, c)</code> doesn't work because you are overwriting the existing <code>x</code> method with an unbound one.
<code>c.x = types.MethodType(c.x, None, c)</code> works because you are overwriting the existing method with a new bound method.

