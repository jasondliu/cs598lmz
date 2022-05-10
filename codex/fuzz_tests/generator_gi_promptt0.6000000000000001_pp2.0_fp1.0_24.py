gi = (i for i in ())
# Test gi.gi_code.co_name
assert next(gi).__name__ == '<genexpr>'

def f():
    def g():
        return
    return g

# Test f().gi_code.co_name
assert f().__name__ == 'g'

class C:
    @staticmethod
    def f():
        pass

# Test C.f.gi_code.co_name
assert C.f.__name__ == 'f'

class D:
    @classmethod
    def f(cls):
        pass

# Test D.f.gi_code.co_name
assert D.f.__name__ == 'f'

class E:
    def __init__(self):
        self.f = lambda: None

# Test E().f.gi_code.co_name
assert E().f.__name__ == '<lambda>'

# Test E().f.__qualname__
assert E().f.__qualname__ == 'E.<locals>.<lambda>'
