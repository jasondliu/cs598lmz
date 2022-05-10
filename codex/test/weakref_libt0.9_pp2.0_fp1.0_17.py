import weakref


class MyClass:
    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return "MyClass(%r)" % self.name


c = MyClass("A")
c_id = id(c)
d = weakref.ref(c)
print(d)
print(d())
print(d() is c)
print(d() is None)

