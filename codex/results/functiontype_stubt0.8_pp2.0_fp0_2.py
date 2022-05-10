from types import FunctionType
a = (x for x in [1])
b = list(a)
type(a), type(b)

def func(a):
    return a

type(func)
def add(a, b):
    return a + b
type(add), tuple(add.__code__.co_varnames)
def _print2(str)"\n", str
type(_print2), _print2.__code__.co_name
def _print3(str, end="\n"):
    print(str, end=end)
_print3("hello world")
import sys

sys.getdefaultencoding()
 
 
code = "def _print(str, end='\\n'):\n    print(str, end=end)"
exec(code)
_print("hello world")
def func(**kwargs):
    return kwargs
func(str=2, b=3, end="\n")
print(code, end="\n") if True else print(1)
if True:
    code = "123"

code
code = "def _print(str, end='
