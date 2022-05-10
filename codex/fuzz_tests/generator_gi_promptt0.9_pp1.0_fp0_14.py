gi = (i for i in ())
# Test gi.gi_code.co_flags with the ! flag
assert not gi.gi_code.co_flags & (1 << 31)
assert gi.gi_code.co_flags == 4
assert gi.gi_code.co_flags == loads(dumps(gi.gi_code.co_flags))
# Test gi.gi_code.co_flags with the other flags
gi = (i for i in xrange(100))
print('Test gi.gi_code.co_flags:')
assert gi.gi_code.co_flags == (1 << 2) + 1 + 4
print(str(gi.gi_code.co_flags))
assert gi.gi_code.co_flags == loads(dumps(gi.gi_code.co_flags))
# Test other code fields and count_stack_items
gi_code = gi.gi_code
assert gi_code.co_argcount == 0
print('Test gi_code.co_nlocals:')
assert gi_code.co_nlocals == 1
print(str(gi_code.
