from types import FunctionType
list(FunctionType(None))
    error
    a=FunctionType(None,(1,2),);list(a)
    a()(1,2)
list(xrange(5))
list(xrange(5,10))
list(xrange(5,10,2))
list(xrange(10,5,-2))
list(xrange(10,5))
list(xrange(10,5,-2))
    1 type(xrange)
    2 range?
filter (lambda x: x%2, xrange(10))
filter(lambda x:x%2,xrange(10))
list(filter(lambda x:x%2,xrange(10)))
filter (lambda , xrange(10))
    error
