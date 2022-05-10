import types
types.ModuleType.__repr__ = lambda self: '<module:{}>'.format(self.__name__)

import sys
sys.modules['__main__'].__file__ = '{}/__main__.py'.format(os.getcwd())

import threading
threading.Thread.__repr__ = lambda self: '<{}({})>'.format(type(self).__name__, self.name)

import re
repr_pattern = re.compile(r'(?<!\\)%')
re.Pattern.__repr__ = lambda self: repr_pattern.sub(r'%%', repr(str(self)))

from collections import deque
deque.__repr__ = lambda self: 'deque([{}])'.format(', '.join(map(repr, self)))

from types import SimpleNamespace
SimpleNamespace.__repr__ = lambda self: 'namespace(**{})'.format(repr(vars(self)))

from types import MappingProxyType
MappingProxyType.__repr__
