import weakref
import re

from . import util

__all__ = [
    'Forward',
    'ForwardContainer',
    'ForwardRef',
]

class Forward(object):
    """
    A Forward instance acts like a weak reference to a type or other object,
    but will not resolve until the target has been defined.
    """
    __slots__ = ['__target', '__callback', '__ref']
    
    def __init__(self, callback=None):
        self.__target = None
        self.__ref = None
        self.__callback = callback
    
    def resolve(self, target):
        """
        Resolve this Forward instance to the given object.
        """
        if self.__callback:
            self.__target = self.__callback(target)
        else:
            self.__target = target
        self.__ref = weakref.ref(self.__target)
    
    def get(self):
        """
        Get the object this Forward instance is a reference to.
        """
        if self.__target is not None:
