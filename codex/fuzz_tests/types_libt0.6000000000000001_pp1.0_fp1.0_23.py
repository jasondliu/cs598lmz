import types
types.MethodType(lambda self: None, None, Foo)()
</code>
But that seems rather hacky and unnecessary, since you can just declare the method in the class:
<code>class Foo:
    def __init__(self):
        pass
</code>
or just
<code>class Foo:
    pass
</code>

