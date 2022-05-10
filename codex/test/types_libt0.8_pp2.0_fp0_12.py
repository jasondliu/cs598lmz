import types
types.ModuleType.__dict__['__reduce__'] = reduce

# ------------------------------------------

import sys
import types

# ------------------------------------------

def __reduce__(self):
    if type(self) == 'module':
        return (getattr, (self, '__dict__'))
    else:
        raise TypeError("Not pickleable")

def dump_to_file(path='/tmp/file.py'):
    with open(path, 'w') as f:
        f.write("""
import pickle
from __reduce__ import __reduce__

class SomeClass:
    def __reduce__(self):
        return (getattr, (__reduce__, '__code__'))

x = types.ModuleType('__reduce__')
x.__dict__['__reduce__'] = __reduce__
pickle.dump(x)
        """)

def main():
    dump_to_file()
    execfile('/tmp/file.py')
