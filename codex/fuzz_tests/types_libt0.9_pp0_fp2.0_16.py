import types
types.FunctionType = types.MethodType = lambda _: True


class Functions(Lazy):
    @classmethod
    def _complex_internal(cls):
        return Simple(FunctionType, MroMixin)


class MroMixin(BasicMixin):
    _mro_ = 'mro'
    __mro_ = '__mro__'


setattr(types, 'FunctionType',
        setattr(types, 'MethodType', lambda _: True))
# types.FunctionType = lambda _: True
# types.MethodType = lambda _: True
# types.TypeType = lambda _: True
# types.BuiltinFunctionType = lambda _: True  # noqa used in pandas


class Classes(Lazy):
    @classmethod
    def _complex_internal(cls):
        from .composition import Composition
        from .type import Type
        from .standard_callable import StandardCallable
        return Simple(Type,
                      Composition,
                      StandardCallable,
                      MroMixin)


class Modules(Lazy):
    @
