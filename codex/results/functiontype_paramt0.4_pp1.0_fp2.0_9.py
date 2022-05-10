from types import FunctionType
list(FunctionType(lambda x: x, globals(), 'lambda_1'))

# code objects
list(__builtins__.compile('[1,2,3]', '', 'eval').co_consts)

# generator objects
list(x for x in [1,2,3])

# class objects
class C(object):
    pass
list(C())

# instance objects
class C(object):
    def __iter__(self):
        yield 1
        yield 2
        yield 3
list(C())

# callable objects
class C(object):
    def __call__(self):
        yield 1
        yield 2
        yield 3
list(C())

# old-style class objects
class C:
    pass
list(C())

# old-style instance objects
class C:
    def __getitem__(self, i):
        if i < 0 or i > 2: raise IndexError
        return i + 1
list(C())

# old-style callable objects
class C:
    def __call__(self):
        yield
