from types import FunctionType
list(FunctionType(globals()['lambda:0:<locals>'].__code__, globals(), 'lambda:0:<locals>'))

from types import CodeType
next(CodeType(globals()['lambda:0:<locals>'].__code__, globals(), 'lambda:0:<locals>', 0))

from types import FunctionType
import types

def walk(item):
    while item:
        item = next(item)
        if type(item) in (FunctionType, types.GeneratorType):
            return item

item = walk(globals()['lambda:0:<locals>'].__code__)
while item:
    item = walk(item)


#from types import CodeType
#CodeType(i.__code__, globals(), 'lambda:0:<locals>', 0, 0, 0, 1)
