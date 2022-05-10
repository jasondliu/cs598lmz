from types import FunctionType
list(FunctionType(f2.__code__,globals(),'',None,(U,),0,None))

#---types------------------------------------------------------------------------------
type(lambda : None)

#---rtype------------------------------------------------------------------------------
def f(x:float)->float:
    return x**2
float_sqr = f
float_sqr.__annotations__ # or f.__annotations__

#---typing_hints----------------------------------------------------------------------
class Student:
    def __init__(self, name:str, age:int) -> None:
        self.name = name
        self.age = age
        self.castrate()
        pass
    def castrate(self):
        self.name:str
        self.age:int
        self.castrate.__annotations__
        return None
 #или
from typing import Callable, Any

def foo(f:Callable[[int], Any])->None:
    pass

foo(lambda i:i+1)

#---typing_3--------------------------------------------------------------------------
from typing import Optional, Iterable
a: Optional[int] = 2

