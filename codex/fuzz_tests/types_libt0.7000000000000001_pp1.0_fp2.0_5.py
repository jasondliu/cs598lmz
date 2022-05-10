import types
types.FunctionType

# The class to which types.FunctionType belongs.
print(types.FunctionType.__class__)

# You can create your own functions with types.FunctionType.
# This example creates a dummy function that accepts no arguments and returns 1.
my_function = types.FunctionType(code=compile('return 1', 'dummy_function', 'eval'), globals={})
print(my_function)
print(my_function())

# You can also create functions from other functions.
# This example creates another dummy function that accepts no arguments and returns 1.
# This time instead of using a code object, we use the code object from the my_function above.
my_function2 = types.FunctionType(code=my_function.__code__, globals={})
print(my_function2)
print(my_function2())

# You can even use the functions you create.
# This example creates a dummy function that accepts no arguments and returns 2.
# This time instead of using a code object, we use the code object from the my_function above.
# The globals parameter is also used
