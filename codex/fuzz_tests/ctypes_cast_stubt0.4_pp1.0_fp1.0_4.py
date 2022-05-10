import ctypes
ctypes.cast(id(obj), ctypes.py_object).value

# 创建一个空的类
class Empty(object):
    pass

# 定义一个接口或者抽象类
from abc import ABCMeta, abstractmethod
class IStream(metaclass=ABCMeta):
    @abstractmethod
    def read(self, maxbytes=-1):
        pass

    @abstractmethod
    def write(self, data):
        pass

# 定义一个接口或者抽象类
from abc import ABC, abstractmethod
class IStream(ABC):
    @abstractmethod
    def read(self, maxbytes=-1):
        pass

    @abstractmethod
    def write(self, data):
        pass

# 实现抽象类
class SocketStream(IStream):
    def read(self, maxbytes=-1):
        pass

   
