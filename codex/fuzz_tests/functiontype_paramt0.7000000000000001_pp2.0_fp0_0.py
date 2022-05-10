from types import FunctionType
list(FunctionType(lambda: 1, globals(), 'lambda'))

class X:
    def __iter__(self):
        yield 1

list(X())

list(iter({'a': 1}))

list(iter(iter(iter({'a': 1}))))

list(iter(iter(iter(iter(iter(iter({'a': 1})))))))

class Y:
    def __await__(self):
        return [1]

list(Y())

list(iter(Y()))

class Z:
    def __aiter__(self):
        return [1]

list(Z())
