from types import FunctionType
a = (x for x in [1])
type(a)

def a():
    pass
type(a)

type(int)
#function
type(type)
type(FunctionType)
type(a)
type(type)
#object класс функций и классов
class A(object):
    pass

type(A)
isinstance(A(),object)

a = A()
type(a)
isinstance(a, A)

a.__class__
class P:
    pass

a = P()
isinstance(a,P)
type(a)

P.__class__
object.__class__
type.__class__
type(P)
type(object)
type(type)
from IPython.core.interactiveshell import InteractiveShell
InteractiveShell.ast_node_interactivity = "all"

a = 0
a.__class__

from types import FunctionType
from types import GeneratorType
from collections import Generator
from collections.abc import Generator
dir(
