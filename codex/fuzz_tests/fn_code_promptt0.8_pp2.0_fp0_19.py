fn = lambda: None
# Test fn.__code__ is not None
print(fn.__code__ is not None) 

# Test fn.__code__ is indeed a code object
print(isinstance(fn.__code__, types.CodeType))

# Test that fn.__code__.co_stacksize > 0
print(fn.__code__.co_stacksize > 0)

# Test that fn.__code__.co_flags & 0x4 != 0
# 0x4 is the flag for CO_NOFREE, which means that no
# free variables (other than cell and free) were found
print(fn.__code__.co_flags & 0x4 != 0)

# Test that fn.__code__.co_nlocals == 0
print(fn.__code__.co_nlocals == 0)

# Test that fn.__code__.co_argcount == 0
print(fn.__code__.co_argcount == 0)

# Print the value of fn.__code__.co_flags
print(bin(fn.__code__.co_flags))

# Print
