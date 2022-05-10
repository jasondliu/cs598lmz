gi = (i for i in ())
# Test gi.gi_code.co_filename
assert gi.gi_code.co_filename == "<stdin>"

def f():
    yield 1

# Test f.func_code.co_filename
assert f.func_code.co_filename == "<stdin>"

# Test f.func_code.co_firstlineno
assert f.func_code.co_firstlineno == 14

# Test f.func_closure
assert f.func_closure == None

# Test f.func_dict
assert f.func_dict == {}

# Test f.func_doc
assert f.func_doc == None

# Test f.func_name
assert f.func_name == "f"

# Test f.func_defaults
assert f.func_defaults == None

# Test f.func_globals
assert f.func_globals == globals()

# Test f.func_code
assert f.func_code.co_argcount == 0
assert f.func_code.co_nlocals == 0
assert f.func_code.co_
