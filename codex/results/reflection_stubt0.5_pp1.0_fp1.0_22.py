fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi.gi_code
fn()

# The following tests are for issue #19356
class C:
    def __init__(self):
        self.counter = -1
    def __iter__(self):
        return self
    def __next__(self):
        self.counter += 1
        if self.counter == 3:
            raise StopIteration
        return self.counter

def f():
    for i in range(3):
        yield i

def f2():
    for i in range(3):
        yield i
    yield from C()

def f3():
    for i in range(3):
        yield i
    yield from f()

def f4():
    for i in range(3):
        yield i
    yield from f2()

def f5():
    for i in range(3):
        yield i
    yield from f3()

def f6():
    for i in range(3):
        yield i
    yield from f4()

def f7():
    for i in range(3):
       
