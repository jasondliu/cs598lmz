from _struct import Struct
s = Struct.__new__(Struct)
s.__init__('i')
s.size

import sys

def __getattr__(name):
    if name == 'stdin':
        import sys
        return sys.stdin
    elif name == 'stdout':
        import sys
        return sys.stdout
    elif name == 'stderr':
        import sys
        return sys.stderr
    else:
        raise AttributeError(name)

def __setattr__(name, value):
    if name == 'stdin' or name == 'stdout' or name == 'stderr':
        raise AttributeError(name)
    else:
        self.__dict__[name] = value

import sys

def __getattr__(name):
    if name == 'stdin':
        import sys
        return sys.stdin
    elif name == 'stdout':
        import sys
        return sys.stdout
    elif name == 'stderr':
        import sys
        return sys.stderr
