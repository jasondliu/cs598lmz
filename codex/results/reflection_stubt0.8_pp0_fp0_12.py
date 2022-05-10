fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi
fn()

# The lower 64 bits of the code object are set to the address of the
# first instruction. This is an address past the end of the builtin
# modules area, so it should be ignored.
code.co_firstlineno = 0x123456789abcdef  # fix first instruction address
fn()

# %s format specifier indicates that the argument is a pointer
print("%s" % code)

# %p format specifier indicates that the argument is a pointer
print("%p" % code)

# The lower 64 bits of the code object are set to the address of the
# first instruction.
# Converts the object referenced by code to an integer. Often used
# for bitwise operations.
print(int(code))

# Prints the integer of the code object
print(hex(code))
