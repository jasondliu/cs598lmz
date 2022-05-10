from types import FunctionType
list(FunctionType(lambda x:x,globals())(range(10)))

# The following is a little more complex.
# It's a function that takes a value and returns a function that returns that value.
# In other words, it "freezes" a value.
# This is useful for passing a value to a function that takes a function as an argument.
# For example, map() takes a function and an iterable.
# If you want to pass a value to map() without using a lambda, you can use the following.
# This is especially useful if the value is complex, like a list.

def freeze(value):
    return lambda: value

map(freeze([1,2,3]), range(10))
# => [[1,2,3], [1,2,3], [1,2,3], [1,2,3], [1,2,3], [1,2,3], [1,2,3], [1,2,3], [1,2,3], [1,2,3]]

# The following is a function that takes a function as an argument and returns a function.
