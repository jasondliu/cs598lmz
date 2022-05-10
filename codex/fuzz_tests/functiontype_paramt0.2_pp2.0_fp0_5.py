from types import FunctionType
list(FunctionType(lambda x: x, globals(), 'lambda'))

# 使用元类
class Meta(type):
    def __new__(cls, name, bases, attrs):
        print(cls, name, bases, attrs)
        return super().__new__(cls, name, bases, attrs)

class A(metaclass=Meta):
    pass

# 使用元类实现单例
class Singleton(type):
    def __init__(cls, *args, **kwargs):
        cls.__instance = None
        super().__init__(*args, **kwargs)

    def __call__(cls, *args, **kwargs):
        if cls.__instance is None:
            cls.__instance = super().__call__(*args, **kwargs)
            return cls.__instance
        else:
            return cls.__instance

class A(metaclass=Singleton):
    pass

a = A()
b =
