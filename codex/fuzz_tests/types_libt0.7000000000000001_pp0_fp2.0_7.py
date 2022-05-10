import types
types.MethodType(f, None,  Bar)
</code>
But this is error prone. There is a better way to do this?


A:

<code>class Bar:
    def f(self):
        return 'Bar'

Bar.f = lambda self: 'Bar'
</code>

