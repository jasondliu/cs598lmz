import types
# Test types.FunctionType
try:
    types.FunctionType
    assert True
except AttributeError:
    skip("No types.FunctionType")

def test_convert_string_to_cstring_with_function(self):
    d = self.space.appexec([self.space.wrap(1.23)], """(w_s):
    return str(w_s)""")
    assert self.space.unwrap(d) == "1.23"

# test the argument parsing logic of __builtin_findmethod_selector()
def test_findmethod_selector():
    from pypy.interpreter import pycode
    from pypy.interpreter.argument import Arguments

    args = Arguments(None, [])
    selector = pycode._findmethod_selector(args, [], [], ['x'], [])
    assert selector is args.firstarg_w()

    args = Arguments(None, [])
    selector = pycode._findmethod_selector(args, [], [], ['x', 'y'], [])
    assert selector
