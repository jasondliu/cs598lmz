import types
# Test types.FunctionType(func_code, func_globals, func_name, func_defaults, func_closure)
@types.trace_calls(grid_size=1000)
def foo(x, a=1, b=2, c=3):
    pass
def bar(x, y):
    informit('bar was entered')
    return x + y
import types
foo_code = types.FunctionType(bar.__code__, globals(), 'foo', foo.__defaults__, foo.__closure__)
# foo(2)
# I found the path on MAC
# /Users/shensq/anaconda3/lib/python3.6/types.py
# Did not find it on Windows
"""


# Save this file as a .py file and run it.
# The book reads very slowly, so 
# I feel free to run the code when I like.

import types
import inspect

def informit(func):
    """
    function decorator to print function details
    before calling
    """

    def wrapper(*args, **kwargs):
        arg
