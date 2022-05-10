import weakref, collections
from code import InteractiveInterpreter
from functools import wraps, partial
from sys import stdin


class MPS(str): 
    """Print an object using its __str__, then the interactive interpreter"""
    
    def __repr__(self):
        string = self.__str__()
        return string+'\n'+InteractiveConsole(locals=self.__dict__).interact(MPS.__doc__)


class Func(object):
    
    def __init__(self, func, arguments=None, deco=[], wraps=None, doc=True):
        self.doc = doc
        self.func = func
        self.arguments = arguments
        self.wraps = weakref.ref(wraps)
        self.__dict__['deco'] = deco
        self.__dict__['deco_data'] = []
    
    
    def __call__(self, *args, **kwargs):
            # return self.func(self.arguments, *args, **kwargs)
        f = self.
