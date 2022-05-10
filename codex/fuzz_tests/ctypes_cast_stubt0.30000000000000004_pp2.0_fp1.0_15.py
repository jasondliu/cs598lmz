import ctypes
ctypes.cast(1, ctypes.py_object)

# 创建一个空类
class MyEmptyClass:
    pass

# 定义一个接口或者抽象类
class IStream(metaclass=ABCMeta):
    @abstractmethod
    def read(self, maxbytes=-1):
        pass

    @abstractmethod
    def write(self, data):
        pass

# 定义一个以某个类作为参数的类
class Spam(metaclass=ABCMeta):
    @property
    @abstractmethod
    def name(self):
        pass

    @name.setter
    @abstractmethod
    def name(self, value):
        pass

    @classmethod
    @abstractmethod
    def method1(cls):
        pass

    @staticmethod
    @abstractmethod
    def method2():
        pass

# 定义
