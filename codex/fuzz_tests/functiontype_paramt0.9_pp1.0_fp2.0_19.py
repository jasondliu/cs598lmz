from types import FunctionType
list(FunctionType("f", globals(), "foo" ).__code__ .co_varnames)

#PYTHON WAY
print("===============Python Way===============")
def f():
    print(red)
    print(blue)
    print(9)
f.__code__ .co_varnames

#PYTHON 3.6 , 3.7
print("===============Python 3.6, 3.7===============")
from inspect import signature
sig = signature(f)
for param in sig.parameters:
    print(param)

#PYTHON 3.5 AND BELOW
print("===============Python 3.5 and below===============")
from inspect import getargspec
getargspec(f)
getargspec(sum)[0]    # no defaults, unlike argspec

# EXECUTE A STRING OF CODE IN THE PAST
print("=================Execute a string of code in past================")
def f():
    red = 9
    f = "Hello!"
    print(red, f)
[i for i in f.__code__.
