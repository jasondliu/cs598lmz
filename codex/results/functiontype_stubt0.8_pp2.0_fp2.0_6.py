from types import FunctionType
a = (x for x in [1])
type(a) is GeneratorType

class A(object):
    def __init__(self):
        pass
    def __call__(self):
        print 'call'
    def __iter__(self):
        yield 'iter'


a = A()
#a.__init__()
a.__call__()
print dir(a)
print type(a)
print type(a.__call__)
print type(a.__call__) is FunctionType
#for i in a:
#    print i

#a = A()
