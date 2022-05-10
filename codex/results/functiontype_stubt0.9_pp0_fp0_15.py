from types import FunctionType
a = (x for x in [1])
isinstance(a, GeneratorType)
# True
isinstance(a, FunctionType)
a = (x for x in [])
isinstance(a, GeneratorType)
# True
isinstance(a, FunctionType)

def func():
    pass
isinstance(func(), GeneratorType)
# False
isinstance(func(), FunctionType)
# True
def func():
    yield 1
isinstance(func(), GeneratorType)
# True
isinstance(func(), FunctionType)
# True

a = [x for x in []]
isinstance(a, GeneratorType)
# False
isinstance(a, FunctionType)
# False
a = [x for x in [1]]
isinstance(a, GeneratorType)
# False
isinstance(a, FunctionType)
# False
</code>
However, we can see that <code>((x for x in []), (x for x in [1]))</code> behaves just like a <code>tuple</code> does, in that it can be accessed by an index and it seems like it has two different elements <code>(element
