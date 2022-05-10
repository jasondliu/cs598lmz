gi = (i for i in ())
# Test gi.gi_code.co_flags
print(gi.gi_code.co_flags & 0x20)

# Test co_flags on code objects
print(gi.gi_code.co_flags & 0x2000)

# Test co_flags on types
print(gi.gi_code.co_flags & 0x20000)

# Test co_flags on functions
print(gi.gi_code.co_flags & 0x40000)

# Test co_flags on methods
print(gi.gi_code.co_flags & 0x80000)

# Test co_flags on classes
print(gi.gi_code.co_flags & 0x100000)

# Test co_flags on generators
print(gi.gi_code.co_flags & 0x400000)

# Test co_flags on coroutines
print(gi.gi_code.co_flags & 0x800000)

# Test co_flags on async generators
print(gi.gi_code.co_flags & 0x1000000)

# Test co_flags on async functions
print(gi.
