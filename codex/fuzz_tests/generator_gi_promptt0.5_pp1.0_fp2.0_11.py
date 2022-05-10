gi = (i for i in ())
# Test gi.gi_code.co_flags
# Should be 0x20
print(gi.gi_code.co_flags)
# Should be 0
print(gi.gi_code.co_argcount)
# Should be 0
print(gi.gi_code.co_kwonlyargcount)
# Should be 0
print(gi.gi_code.co_nlocals)
# Should be 0
print(gi.gi_code.co_stacksize)
# Should be 0
print(gi.gi_code.co_flags)
# Should be 0
print(gi.gi_code.co_firstlineno)
# Should be '<genexpr>'
print(gi.gi_code.co_name)
# Should be ()
print(gi.gi_code.co_varnames)
# Should be ()
print(gi.gi_code.co_freevars)
# Should be ()
print(gi.gi_code.co_cellvars)
# Should be '<code object <genexpr> at 0x7f0f7e7b9e30, file "<std
