from types import FunctionType
a = (x for x in [1])
type(a)

def func():
    pass

type(func)
type(lambda x:x)
type(abs)
type(123)

type('123')
type(b'123')
type(u'123')

type(type)
type(dir)
type(None)

class Test:
    pass

type(Test)
type(Test())
type(Test) == type(Test())

type(Test) == object

type(Test()) == object
