gi = (i for i in ())
# Test gi.gi_code is equivalent
def tgen_code(gi):
    return gi[0]
def tfunc_code(func):
    return func.__code__
assert tgen_code(gi) is tfunc_code(tgen_code)
class MyGen(object):
    def __iter__(self):
        yield 1
        return
    def close(self):
        pass
def tfunc():
    yield 1
    return
mg = MyGen()
assert hasattr(mg, 'close')
assert not hasattr(tfunc(), 'close')
class MyIter(object):
    def __init__(self):
        self.i = 0
    def __iter__(self):
        return self
    def __next__(self):
        self.i += 1
        if self.i > 10:
            raise StopIteration(self.i)
        return self.i
def tgen():
    for i in range(1, 11):
        yield i
mi = MyIter()
gi = tgen()
for x, y in zip(mi, gi):
    assert
