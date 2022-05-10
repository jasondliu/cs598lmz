from types import FunctionType
list(FunctionType('foo'))

def foo():
    print('foo')

list(foo)

def bar(args):
    print('bar')

list(bar('args'))
