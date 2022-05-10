gi = (i for i in ())
# Test gi.gi_code
try:
    gi.gi_code
except AttributeError:
    print("SKIP")
    raise SystemExit

print(gi.gi_code.co_argcount)
print(gi.gi_code.co_code)
print(gi.gi_code.co_filename)
print(gi.gi_code.co_firstlineno)
print(gi.gi_code.co_flags)
print(gi.gi_code.co_freevars)
print(gi.gi_code.co_lnotab)
print(gi.gi_code.co_name)
print(gi.gi_code.co_names)
print(gi.gi_code.co_nlocals)
print(gi.gi_code.co_stacksize)
print(gi.gi_code.co_varnames)
