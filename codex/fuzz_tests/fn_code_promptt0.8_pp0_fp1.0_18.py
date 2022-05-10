fn = lambda: None
# Test fn.__code__.co_filename, fn.__code__.co_firstlineno and fn.__code__.co_name
print("1. Code Object from anonymous function:")
print("File path:", fn.__code__.co_filename)
print("Function name:", fn.__code__.co_name)
print("First line no:", fn.__code__.co_firstlineno)

fn = lambda x, y: x + y
# Test fn.__code__.co_argcount, fn.__code__.co_varnames
print("\n2. Code Object from lambda-expression:")
print("Argument count:", fn.__code__.co_argcount)
print("Argument names:", fn.__code__.co_varnames)


def fn(x, y):
    return x + y


# Test fn.__code__.co_argcount
print("\n3. Code Object from function definition:")
print("Argument count:", fn.__code__.co_argcount)
