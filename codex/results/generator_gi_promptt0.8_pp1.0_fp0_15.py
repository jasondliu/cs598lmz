gi = (i for i in ())
# Test gi.gi_code.co_flags

if isinstance(gi, types.GeneratorType):
    print('Generator gi:')
    print('  gi_code:')
    print('    co_argcount', gi.gi_code.co_argcount)
    print('    co_kwonlyargcount', gi.gi_code.co_kwonlyargcount)
    print('    co_nlocals', gi.gi_code.co_nlocals)
    print('    co_stacksize', gi.gi_code.co_stacksize)
    print('    co_flags', gi.gi_code.co_flags, bin(gi.gi_code.co_flags))
    print()

# Test gi.gi_frame.f_lasti

print('gi.gi_frame:')
print('  f_lasti', gi.gi_frame.f_lasti)
print()

# Test gi.gi_frame.f_locals

print('gi.gi_frame:')
print('  f_locals
