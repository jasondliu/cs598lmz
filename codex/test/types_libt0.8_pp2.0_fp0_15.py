import types
types.FunctionType
type(len)
type(lambda x: x)
type(x for x in range(10))

hasattr(object, "__len__")

isinstance("abc", (str, bytes))

import numbers
isinstance(10, numbers.Integral)

# Metaclass

class Meta(type):
    pass

class MyClass(metaclass=Meta):
    pass

# Metaclasses, super()

class Base:
    def foo(self):
        return "foo"

class Derived(Base):
    def bar(self):
        return super().foo()

class Mapping:
    def __init__(self, iterable):
        self.items_list = []
        self.__update(iterable)

    def update(self, iterable):
        for item in iterable:
            self.items_list.append(item)

    __update = update   # private copy of original update() method

