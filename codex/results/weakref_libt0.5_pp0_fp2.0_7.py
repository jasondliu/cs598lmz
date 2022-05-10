import weakref
from . import _core

TRAIT_TYPES = {
    'c': 'str',
    'b': 'bool',
    'i': 'int',
    'u': 'int',
    'f': 'float',
    's': 'str',
    't': 'str',
    'e': 'Enum',
    'v': 'Color',
    'z': 'Complex',
    'm': 'BaseTuple',
    'x': 'Any',
    'o': 'Instance',
    'd': 'Callable',
    'r': 'Range',
    'l': 'List',
    'a': 'Array',
    'D': 'Dict'
}

TRAIT_PREFIXES = {
    'c': 'C',
    'b': 'B',
    'i': 'I',
    'u': 'U',
    'f': 'F',
    's': 'S',
    't': 'T',
    'e': 'E',
    'v': 'V',
   
