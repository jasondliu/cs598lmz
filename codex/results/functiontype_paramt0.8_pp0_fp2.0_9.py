from types import FunctionType
list(FunctionType(lambda:None).__code__.co_consts)

def fact(n):
    if n==0:
        return 0
    return n*fact(n-1)
fact(3)
fact(3)
import dis
dis.dis(fact)
from types import FunctionType
list(FunctionType(lambda:None).__code__.co_consts)

def test(x,y):
    if x==0:
        return 1
    return x*test(x-1,y+1)
list(FunctionType(test).__code__.co_varnames)
list(FunctionType(test).__code__.co_argcount)
test.__code__.co_argcount

from types import FunctionType
list(FunctionType(lambda:None).__code__.co_consts)
dis.dis(test)
from types import FunctionType
list(FunctionType(lambda:None).__code__.co_consts)

def test(x,y):
    if x==0:
        return 1
    return x*test(x-
