from types import FunctionType
list(FunctionType(lambda x: x, globals(), 'lambda')
     for x in range(10))

# <codecell>

# A lambda that returns a lambda
def make_adder(n):
    return lambda x: x + n

plus_3 = make_adder(3)
plus_5 = make_adder(5)

plus_3(4)

# <codecell>

# A lambda that returns a lambda that returns a lambda
def make_adder(n):
    return lambda x: lambda y: x + y + n

plus_3 = make_adder(3)
plus_3(4)(5)

# <codecell>

# A lambda that returns a lambda that returns a lambda that returns a lambda
def make_adder(n):
    return lambda x: lambda y: lambda z: x + y + z + n

plus_3 = make_adder(3)
plus_3(4)(5)(6)

# <codecell>

# A lambda that returns a lambda that returns a lambda that returns a lambda that returns a lambda
def make_adder(
