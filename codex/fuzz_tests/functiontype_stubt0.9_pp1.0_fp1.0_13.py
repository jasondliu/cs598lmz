from types import FunctionType
a = (x for x in [1])
b = (x for x in a)
c = (x for x in b)
isinstance(c, types.GeneratorType)

def g(x):
    yield x + 1
    yield x + 2
    
isinstance(g(1), type(a))
isinstance(g(1), type(b))
# isinstance(g(1), type(c)) >>> error using type! use isinstance() instead
isinstance(g(1), types.GeneratorType)
isinstance(a, types.GeneratorType)
import inspect
inspect.isgenerator(a)
inspect.isgenerator(1)
type((x for x in []))

# more with generators
def add_ten(numbers):
    for n in numbers:
        yield n + 10

numbers = [1,2,3,4,5]
add_ten(numbers)

# for n in add_ten(numbers):
#     print(n)

def numbers_which_are_greater_than_three(numbers):
    for n in numbers
