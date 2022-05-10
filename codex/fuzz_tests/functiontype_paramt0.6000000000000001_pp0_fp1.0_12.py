from types import FunctionType
list(FunctionType(lambda x: 2*x, globals(), 'doubler') for x in range(5))

# Generator loop
# The code in the loop body is not run at the time the generator is created,
# but when the loop calls next() on the generator,
# the generator's code starts executing.
# The local state of the function is saved between calls
# so that the function can continue execution.
def spin_loop(n):
   i = 0
   while i < n:
      yield i
      i += 1

# Generator functions and expressions can be used in the same ways as you have used other iterables.
# For example, you can iterate over them with a for loop,
# or pass them to any other function that consumes an iterable.

# Functions that return generators are also referred to as coroutines.
# A coroutine is a function that can be paused and resumed.

# Generator expressions are similar to list comprehensions,
# except that they return a generator object instead of a list.
# To create a generator expression, use parentheses instead of square brackets.

# Generator expressions have the same performance advantages as
