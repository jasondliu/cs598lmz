from types import FunctionType
list(FunctionType(lambda: None, globals(), 'lambda'))

# __call__
class Callable:
    def __call__(self, *args, **kwargs):
        print('called')

Callable()()

# __getattr__
class GetAttr:
    def __getattr__(self, name):
        if name == 'age':
            return 40
        else:
            raise AttributeError(name)

GetAttr().age

# __getattribute__
class GetAttribute:
    def __getattribute__(self, name):
        print('get:', name)
        return super().__getattribute__(name)

GetAttribute().age

# __setattr__
class SetAttr:
    def __setattr__(self, name, value):
        if name == 'age':
            self.__dict__[name] = value
        else:
            raise AttributeError(name)

SetAttr().age = 40

# __delattr__
class DelAttr:
    def __delattr__(self, name):
        if
