from types import FunctionType
list(FunctionType(lambda x: x, globals()) for x in range(3))

# list comprehensions
# [ expression for item in list if conditional ]

# list comprehensions - with conditional
[x for x in range(5) if x % 2 == 0]

# list comprehensions - with conditional and else
[x if x % 2 == 0 else -1 for x in range(5)]

# list comprehensions - nested
[x+y for x in [10,30,50] for y in [20,40,60]]

# list comprehensions - nested with conditional
[x+y for x in [10,30,50] for y in [20,40,60] if x+y < 100]

# list comprehensions - nested with conditional and else
[x+y if x+y < 100 else 'BIG' for x in [10,30,50] for y in [20,40,60]]

# list comprehensions - nested with conditional and else and functions
[x+y if x+y < 100 else 'BIG' for x in [10,30,50] for y in [
