import types
types.FunctionType(lambda: 0, {}, "foo", (), None)

def foo():
    pass

foo.__name__

"""
>>> types.FunctionType(lambda: 0, {}, "foo", (), None)
<function <lambda> at 0x7f7e6b8ee400>
>>> def foo():
...     pass
...
>>> foo.__name__
'foo'
>>>
"""
