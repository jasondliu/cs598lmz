from types import FunctionType
list(FunctionType(lambda x: x*x, globals())(x) for x in range(20))

# Multiple for statements
[x for x in range(20) if x % 2 == 0 for y in range(5) if y > 2]

# Multiple if statements
[x for x in range(20) if x % 2 == 0 if x % 3 == 1]

# Dictionary comprehensions
{x: x*2 for x in range(5)}

# Set comprehensions
{x for x in range(10) if x % 2 == 0}

# Generator comprehensions
(x for x in range(10) if x % 2 == 0)
next(gen)
next(gen)

# Generator expression
(x * 2 for x in range(20))

# Nested comprehensions
list(list(x * y for y in range(1, 11)) for x in range(1, 11))

# Parentheses are optional
[x * 2 for x in range(20)]

# Using the comprehension as an argument
list(x * 2 for x in range(20))

# Using the
