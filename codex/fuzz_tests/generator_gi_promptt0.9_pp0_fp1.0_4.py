gi = (i for i in ())
# Test gi.gi_code
import types

# Test whether line numbers in tracebacks are correct for generators
# with a try:finally block (see issue #5748).
def gen():
    try:
        yield None
    finally:
        pass
g = gen()

try:
    g.send(1)
except TypeError:
    pass
# Test subclasses with custom gi_code
class MyIter(object):
    def __init__(self, x):
        self.x = x
    def __next__(self):
        self.x -= 1
        if self.x <= 0:
            raise StopIteration
        return self.x

class MySubIter(MyIter):
    __next__ = MyIter.__next__
    def next(self):
        return MyIter.__next__(self)
    def __iter__(self):
        return self

def function():
    for i in MySubIter(10):
        yield i

it = function()
# Test whether yields from another generator
def foo():
    for i in range(10):
        yield i
