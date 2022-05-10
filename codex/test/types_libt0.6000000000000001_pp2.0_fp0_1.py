import types
types.new_class

import abc
class Base(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def foo(self):
        pass
    @abc.abstractmethod
    def bar(self):
        pass

# Base.register(tuple)

# isinstance((), Base)

# issubclass(tuple, Base)

# Base.__subclasses__()

# from collections import abc
# isinstance((), abc.Sequence)

import numbers

def clip(text, max_len=80):
    """在max_len前面或后面的第一个空格处截断文本
    """
    end = None
    if len(text) > max_len:
        space_before = text.rfind(' ', 0, max_len)
        if space_before >= 0:
            end = space_before
        else:
            space_after = text.rfind(' ', max_len)
