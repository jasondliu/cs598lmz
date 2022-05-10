gi = (i for i in ())
# Test gi.gi_code
print(gi.gi_code)
print(gi.gi_code.co_name)
print(gi.gi_code.co_filename)
print(gi.gi_code.co_firstlineno)
print(gi.gi_code.co_argcount)
print(gi.gi_code.co_flags)
print(gi.gi_code.co_code)
print(gi.gi_code.co_consts)
print(gi.gi_code.co_names)
print(gi.gi_code.co_varnames)
print(gi.gi_code.co_freevars)
print(gi.gi_code.co_cellvars)

def f():
    pass

print(f.__code__.co_code)
print(f.__code__.co_consts)
print(f.__code__.co_names)
print(f.__code__.co_varnames)
print(f.__code__.co_freevars)
print(f.__code__.co_cellvars
