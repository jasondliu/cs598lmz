import types
# Test types.FunctionType and types.LambdaType

def check(type, obj, name, docstring):
    assert isinstance(obj, type), "%r is not a %s" % (obj, type)
    assert obj.__name__ == name, "%r has wrong name" % obj
    if docstring is not None:
        assert obj.__doc__ == docstring, "%r has wrong docstring" % obj
    
def check_bad(type, obj, name):
    try:
        check(type, obj, name, None)
    except AssertionError:
        return
    assert 0, "%r IS a %s" % (obj, type)

# Compile a function of each type.

def makefunc(code, type, name):
    if type is types.FunctionType:
        d = {'name': name}
        exec code in d
        return d['test']
    if type is types.LambdaType:
        return eval(code)


code = """\
def test(x):
    return x
"""

for t in types.FunctionType
