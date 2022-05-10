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
