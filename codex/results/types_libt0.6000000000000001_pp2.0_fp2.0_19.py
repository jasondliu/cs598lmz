import types
types.MethodType(__new__, None, None)

# doesn't work:
#types.MethodType(__new__, None, None)
#__new__(None, None)
#type.__new__(None, None)
</code>
I'm not sure how to get around this


A:

<code>__new__</code> is a static method, not a bound method.  You can't call it on an instance.
You probably want to call the <code>object.__new__</code> method itself.  You could do this using <code>types.MethodType</code> to make a bound method, but there's no need to use <code>types</code> at all; just call the method directly.
<code>object.__new__(type, name, bases, dct)
</code>

