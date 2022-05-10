from types import FunctionType
list(FunctionType(lambda x: x, globals())(x) for x in range(5))

# using a generator expression
list((lambda x: x)(x) for x in range(5))

# using a list comprehension
[(lambda x: x)(x) for x in range(5)]

# using a dict comprehension
{x: (lambda x: x)(x) for x in range(5)}

# using a set comprehension
{(lambda x: x)(x) for x in range(5)}

# using a generator expression
(lambda x: x)(x) for x in range(5)

# using a list comprehension
[(lambda x: x)(x) for x in range(5)]

# using a dict comprehension
{x: (lambda x: x)(x) for x in range(5)}

# using a set comprehension
{(lambda x: x)(x) for x in range(5)}

# using a generator expression
(lambda x: x)(x) for x in range(5)

# using a list comprehension
[(lambda x: x)(x) for x
