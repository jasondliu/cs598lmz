from types import FunctionType
a = (x for x in [1])
b = [x for x in [1]]
c = {x for x in [1]}
d = {x: x for x in [1]}
e = FunctionType(lambda x: x, globals())
f = FunctionType(lambda x: x, globals())
g = FunctionType(lambda x: x, globals())
h = FunctionType(lambda x: x, globals())
"""
    )
    assert result.exit_code == 0
    assert "9 errors" in result.output
    assert "8 warnings" in result.output
    assert (
        "W08: 'a' is a generator which does not get iterated over." in result.output
    )
    assert "W08: 'b' is a list comprehension." in result.output
    assert "W08: 'c' is a set comprehension." in result.output
    assert "W08: 'd' is a dictionary comprehension." in result.output
    assert "W08: 'e' is a lambda." in result.output
    assert "W08: 'f' is a function." in result.output
    assert
