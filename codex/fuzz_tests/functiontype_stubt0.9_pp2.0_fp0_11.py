from types import FunctionType
a = (x for x in [1])
type(a)

FunctionType
import types
isinstance(max,types.BuiltinFunctionType)
isinstance(abs,types.BuiltinFunctionType)

from abc import ABCMeta,abstractmethod
from random import randint
from collections import Mapping
class Tombola(metaclass=ABCMeta):
    @abstractmethod
    def load(self,iterable):
        '''iterable is iterable object'''

    @abstractmethod
    def pick(self):
        '''return a random item and remove '''

    def loaded(self):
        '''if load any object return True,else return False'''
        return bool(self.inspect())

    def inspect(self):
        '''return a sorted tuple'''
        items = []
        while True:
            try:
                items.append(self.pick())
            except LookupError:
                break
        return tuple(sorted(items))

    @classmethod
    def __subclasshook__(class_,subclass):
        if class_ is Tombola:
            if (any
