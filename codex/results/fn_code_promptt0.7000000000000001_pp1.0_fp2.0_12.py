fn = lambda: None
# Test fn.__code__.co_filename

@asyncio.coroutine
def coro():
    yield from []
# Test coro.__code__.co_filename

def f():
    return f.__code__.co_filename

mod = types.ModuleType('mod')
mod.__file__ = 'a.py'

class C():
    def m(self):
        return m.__code__.co_filename

class D():
    def m(self):
        return m.__code__.co_filename

class E():
    def __init__(self):
        self.e = __file__

class F():
    def __getattr__(self, name):
        return 'F.__getattr__'

class G():
    @property
    def g(self):
        return __file__

class H():
    @property
    def h(self):
        return __file__

class I():
    @property
    def i(self):
        return __file__

class J(I):
    @property
    def
