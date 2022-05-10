from types import FunctionType
list(FunctionType(lambda x: x, globals(), 'lambda'))

# 使用元类
class MyMeta(type):
    def __new__(cls, name, bases, attrs):
        print(cls, name, bases, attrs)
        return super().__new__(cls, name, bases, attrs)

class MyClass(metaclass=MyMeta):
    pass

# 使用元类实现单例模式
class Singleton(type):
    def __init__(self, *args, **kwargs):
        self.__instance = None
        super().__init__(*args, **kwargs)

    def __call__(self, *args, **kwargs):
        if self.__instance is None:
            self.__instance = super().__call__(*args, **kwargs)
            return self.__instance
        else:
            return self.__instance

class MyClass(metaclass=Singleton):
    pass

# 使用
