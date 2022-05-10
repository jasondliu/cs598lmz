from _struct import Struct
s = Struct.__new__(Struct)
dir(s)

getattr(s, 'pack')

import operator
import os
getattr(operator, 'add')
os.path.split

import operator
import sys
def get_func(name, module=operator):
    if module is None:
        module = sys.modules[__name__]
    return getattr(module, name)
