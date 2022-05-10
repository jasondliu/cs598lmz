import types
types.TracebackType

class Foo():

    def __new__(cls, *args, **kwargs):
        o = object.__new__(cls)
        o.__init__(*args, **kwargs)

class Foo2():

    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    class_attr = 10

    def func(self):
        return self.x + self.y + self.z

f = Foo(1, 2, 3)
print(f.x)
# OUT: 1


g = Foo2(1, 2, 3)
print(type(Foo2.class_attr))
# OUT: &lt;type 'int'&gt;
print(type(g.func))
# OUT: &lt;type 'instancemethod'&gt;

print(type(None))
# OUT: &lt;type 'NoneType'&gt;

print(f.__class__)
# OUT: &lt;class '__main
