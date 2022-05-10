import types
types.MethodType(testint, 5)

# Unbound methods are not supported:
def test_unbound():
    class Foo:
        def bar(self):
            pass
    Foo.bar == Foo.bar
