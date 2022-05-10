from types import FunctionType
list(FunctionType('_', '_', '_', None).__annotations__.keys())


def func(*args, **kwargs):
    return args, kwargs


func.__annotations__
func.__kwdefaults__


# 描述器
class Descriptor:
    def __get__(self, instance, owner):
        pass

    def __set__(self, instance, value):
        pass

    def __delete__(self, instance):
        pass


# 描述器 实现
from weakref import WeakKeyDictionary


class NonNegative:
    def __init__(self, default):
        self.default = default
        self._data = WeakKeyDictionary()

    def __get__(self, instance, owner):
        return self._data.get(instance, self.default)

    def __set__(self, instance, value):
        if value < 0:
            raise ValueError('Must be >= 0')
        self._data[instance] = value

    def __delete__(self,
