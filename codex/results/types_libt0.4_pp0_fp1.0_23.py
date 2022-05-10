import types
types.MethodType(func, None, class_name)
</code>
But I'm getting:
<code>TypeError: unbound method func() must be called with class_name instance as first argument (got nothing instead)
</code>
How can I do this?


A:

<code>def func(self, *args, **kwargs):
    pass

class_name = type('class_name', (object,), {})

class_name.func = types.MethodType(func, class_name)
</code>

