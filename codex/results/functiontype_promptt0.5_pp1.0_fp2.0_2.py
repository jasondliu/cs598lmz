import types
# Test types.FunctionType
import sys
import imp
import marshal

def dump(x):
    print type(x), repr(x)

def make_function(code, globs=None, name="<unknown>"):
    """Make a function object from a code object and a dictionary."""
    return types.FunctionType(code, globs, name)

def main():
    # Test marshal
    # Create a function object from marshal data
    co = compile("x+1", "?", "eval")
    dump(co)
    co = marshal.dumps(co)
    co = marshal.loads(co)
    dump(co)
    f = make_function(co, globals())
    dump(f)
    print f(2)

    # Test pickle
    # Create a function object from pickle data
    import pickle
    co = compile("x+1", "?", "eval")
    dump(co)
    co = pickle.dumps(co)
    co = pickle.loads(co)
    dump(co)
    f = make_
