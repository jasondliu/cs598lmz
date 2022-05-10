import gc, weakref


class Foo:
    def __init__(self, name) -> None:
        self.name = name

    def __del__(self):
        print("del foo...", self.name)


foo = Foo("John")
print(foo)
bar = foo
foo = 'hehe'
del bar
print("*" * 20)
del foo
print("*" * 20)
gc.collect()
print("*" * 20)

print("*" * 20)


class Foo:
    def __init__(self, name) -> None:
        self.name = name

    def __del__(self):
        print("del foo...", self.name)


foo = Foo("John")
print(foo)
bar = weakref.ref(foo)
print(bar)
foo = "hehe"
print(bar())
print("*" * 20)

print("*" * 20)


class Foo:
    def __init__(self, name) -> None:
        self.name = name

