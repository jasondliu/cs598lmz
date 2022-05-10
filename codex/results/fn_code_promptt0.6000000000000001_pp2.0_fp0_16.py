fn = lambda: None
# Test fn.__code__.co_firstlineno
fn.__code__.co_firstlineno

# Test closure cell
def f(x):
    if x > 0:
        def g(y):
            return x * y
        return g
    else:
        return lambda y: y

f(3)(4)

# Test tuple assignment
def g(x, y):
    x, y = y, x
    return x, y

g(1, 2)

# Test list comprehension
[x*x for x in range(10)]

# Test dict comprehension
{x: x*x for x in range(10)}

# Test set comprehension
{x*x for x in range(10)}

# Test generator comprehension
(x*x for x in range(10))

# Test nested comprehensions
[[x*x for x in range(y)] for y in range(10)]

# Test nested comprehensions with lambda functions
[[lambda x: x*x for x in range(y)] for y in range(10)]

# Test nested comprehensions with list.append
[[
