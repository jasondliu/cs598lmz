from _struct import Struct
s = Struct.__new__(Struct)
print(s.format)

s.format = '>I'
print(s.size)

# 2.11 使用@property
class Person(object):
    def __init__(self,first_name):
        self.first_name = first_name
    #Getter function
    @property
    def first_name(self):
        return self._first_name

    @first_name.setter
    def first_name(self,value):
        if not isinstance(value,str):
            raise TypeError('Expected a string')
        self._first_name = value

    # Deleter
    @first_name.deleter
    def first_name(self):
        raise AttributeError('can not delete attribute')

a = Person('Guido')
print(a.first_name)
a.first_name = 42

# 2.12 定义抽象基类
from abc import ABCMeta, abstractmethod
