from types import FunctionType
a = (x for x in [1])
b = [lambda x: x for x in range(10)]
c = (x for x in range(10))
d = map(lambda x: x, range(10))
e = (x for x in range(10))
f = {lambda x: x: 2 for x in range(10)}
g = [1,2,3]
type(a)
type(b)
type(c)
type(d)
type(e)
isinstance(a, GeneratorType)
isinstance(b, GeneratorType)
type(f.values()[0])
isinstance(f.values()[0], FunctionType)
type(g)
isinstance(g, GeneratorType)
type(g) is GeneratorType
 

type(type([]))
 

 
class A(object):
    def __init__(self):
        self.x = 1
        self._x = 2
        __x = 3
        super().__init__
        super(A, self).__init__
        
a = A()
a.x, a._x
 
def
