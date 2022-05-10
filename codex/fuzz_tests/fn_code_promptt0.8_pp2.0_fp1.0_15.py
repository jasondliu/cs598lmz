fn = lambda: None
# Test fn.__code__
print('fn.__code__:', fn.__code__)
print('fn.__code__.co_name:', fn.__code__.co_name)
print('fn.__code__.co_varnames:', fn.__code__.co_varnames)
print('fn.__code__.co_argcount:', fn.__code__.co_argcount)

print()


# Other types of objects
import math
print('math.__code__:', math.__code__)
print('math.__code__.co_name:', math.__code__.co_name)
print('math.__code__.co_varnames:', math.__code__.co_varnames)
print('math.__code__.co_argcount:', math.__code__.co_argcount)

# Test type(1)
print('type(1):', type(1))
print('type(1).__code__:', type(1).__code__)

# Test len
print('len.__code__
