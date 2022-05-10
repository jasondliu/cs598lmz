fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi.__code__
fn.__code__()  # Fails with AttributeError: 'generator' object has no attribute 'co_code'


# This shows that a function object does not actually need to hold a
# callable object. All that needs to be present is a __code__ attr.

# As a consequence of this you can do some cool things like:

import builtins
builtins.abs = lambda x: -x
print(abs(1))  # Prints -1


# In general, functions behave like objects. This is because they are
# objects. So you can do crazy things like:

def add_numbers(number1, number2):
    return number1 + number2


def call_function_with_keywords(function, **kwargs):
    return function(**kwargs)


print(call_function_with_keywords(add_numbers, number1=1, number2=2))


# This is something you'd only ever do in a test suite to test the functionality
# of a function when passed keywords.
