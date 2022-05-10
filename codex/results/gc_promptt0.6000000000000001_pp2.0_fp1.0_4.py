import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect() in a function with an argument.
def func(arg):
    gc.collect()

# Test gc.collect() in a function called in a loop.
def test_loop():
    while 1:
        try:
            yield
        except GeneratorExit:
            gc.collect()
            return
# Test gc.collect() in a class method.
class Foo(object):
    def __init__(self):
        self.x = 42
    def bar(self):
        gc.collect()
    def bar2(self):
        self.x = gc.collect()

a = Foo()

# Test gc.collect() in a coroutine.
def test_coroutine():
    yield 42
    gc.collect()
    yield

# Test gc.collect() on the stack.
def test_stack():
    x = [1,2,3]
    x.append(x)
    # Test gc.collect() in a nested function.
    foo = lambda : gc.collect()
    foo()
    gc.collect()
