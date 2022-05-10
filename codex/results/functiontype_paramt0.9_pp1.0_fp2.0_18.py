from types import FunctionType
list(FunctionType(lambda **kw: (print(kw), 42), [], {}))

# custom class
class MyList(list):
    def __getitem__(self, pos):
        return 999

list(MyList([1, 2, 3]))

# custom callable function
def myfunc():
    yield 1
    yield 2
    yield 3

list(myfunc())
# list(myfunc()[10]) # raises IndexError
# list(myfunc()[10:32]) # raises IndexError

# itertools
import itertools
list(itertools.count(start=10, step=2))
list(itertools.repeat(42, times=3))
list(itertools.cycle([1, 1, 1, 2]))
list(itertools.accumulate([1, 1, 1, 2], operator.mul))
list(itertools.chain(range(3), range(1, 22)))
list(itertools.chain.from_iterable([range(3), range(1, 22)]))
list(itertools.product
