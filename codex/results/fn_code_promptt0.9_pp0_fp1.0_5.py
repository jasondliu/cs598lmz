fn = lambda: None
# Test fn.__code__
print(f'The variable of f is {type(f)},')
print(f'f type code is {type(f.__code__)}')
fn.__code__ = f.__code__
setattr(fn, '__code__', f.__code__)
print(f'After setting the function fn to having the same __code__, fn type is {type(fn.__code__)}')


print(fn.__code__.co_argcount)
print(fn.__code__.co_varnames)
print(fn.__code__.co_names)
print(fn.__code__.co_filename)
print(fn.__code__.co_stacksize)
print(fn.__code__.co_nlocals)
print(fn.__code__.co_firstlineno)

print('\n')
print('Generating a new function based on only two attributes')
def test_funcion():
    print('This is from the test function')
print(f'The argument of test_function is {test_funcion.__
