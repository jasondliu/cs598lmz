fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi

# Code objects support the attribute co_code, which is a string representing
# the sequence of bytecode instructions and their arguments.

import dis

def f(): pass

co = f.__code__
dis.dis(co)

print(co.co_code)
print(len(co.co_code))

# Each instruction is one (or sometimes more) bytes. The leftmost 2 bits of
# the byte indicate the type of instruction:
#
#   00: LOAD_FAST
#   01: STORE_FAST
#   10: DELETE_FAST
#   11: UNARY_NOT
#
# The remaining 6 bits are an unsigned index into co_varnames. In this case,
# the index is 1, which refers to “b”.

# Because code is just a sequence of bytes and integers, it is easy for a
# function to have a reference to another function’s code. When this happens,
# the names in the “constants” tuple and the names in co_names refer to the
# same objects.
