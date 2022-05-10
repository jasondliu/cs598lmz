import types
types.MethodType(func, None, cls)

# TypeError: unbound method func() must be called with cls instance as first argument (got nothing instead)
</code>
But if you do:
<code>types.MethodType(func, cls, cls)
</code>
it works.

