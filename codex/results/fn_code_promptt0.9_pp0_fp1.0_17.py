fn = lambda: None
# Test fn.__code__.co_filename
test_fn.__code__.co_filename

# Assign the function block identifier of test_fn to test_fn_code_id
test_fn_code_id = test_fn.__code__.co_firstlineno

# Print the test_fn_code_id
print(test_fn_code_id)

# Print the code block `__code__.co_filename` attribute
print(test_fn.__code__.co_filename)

# Basic syntax of closure
def outer_func():
    x = 2
    def inner_func(x=x):
        print(x)
    inner_func()
outer_func()

# Example of nonlocal
def outer_func():
    x = 2
    def inner_func():
        nonlocal x
        x = 5
    inner_func()
    return x
print(outer_func())

# Defining nested functions
def outer_function():
    x = 2
    print('outer nonlocal before:', x)

    def inner_function():
        nonlocal x

