import types
types.MethodType(lambda self: self.value, None, Foo)

# classmethod
Foo.value = 5
Foo.value = types.MethodType(lambda cls: cls.value, None, Foo)
Foo().value()

# staticmethod
Foo.value = 6
Foo.value = types.FunctionType(lambda: Foo.value, {}, 'value')
Foo.value()

# property
Foo.value = 7
Foo.value = property(lambda self: self._value)
Foo.value = property(lambda self: self._value, lambda self, v: setattr(self, '_value', v))
Foo().value
Foo().value = 8
Foo().value

# descriptor
class Value:
    def __get__(self, instance, owner):
        return instance._value
    def __set__(self, instance, value):
        instance._value = value
Foo.value = Value()
Foo().value
Foo().value = 9
Foo().value

# data descriptor
class Value:
    def __
