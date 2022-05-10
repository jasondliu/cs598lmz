from types import FunctionType
list(FunctionType(lambda x: x, globals()) for x in range(10))

# In Python 2.6, the list comprehension would return an iterator,
# not an actual list.

# In Python 2.7, the list comprehension returns a list.

# In Python 3.x, the list comprehension returns a generator.

# In Python 2.6, there is no need to use a generator expression
# in order to get an iterator.

# In Python 2.7, a generator expression is necessary in order to get
# an iterator.

# In Python 3.x, a generator expression is necessary in order to get
# a generator.

# In Python 2.6, the generator expression does not have to be parenthesized.

# In Python 2.7, the generator expression must be parenthesized.

# In Python 3.x, the generator expression must be parenthesized.

# In Python 2.6, a generator expression can be used in a lambda.

# In Python 2.7, a generator expression cannot be used in a lambda.

# In Python 3.x, a generator expression cannot be used in
