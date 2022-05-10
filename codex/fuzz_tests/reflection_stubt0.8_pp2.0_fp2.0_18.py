fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi
fn()

class BadClass(object):
    def __getattribute__(self, name):
        return globals()[name]

BadClass().__code__ = gi
BadClass().__code__()

class BadClass2(object):
    def __getattr__(self, name):
        return globals()[name]

BadClass2().__code__ = gi
BadClass2().__code__()

f = lambda: None
gi.gi_code = gi
f.func_code = gi
f()

gi.gi_code = gi
gi.gi_frame = gi
gi.gi_running = gi
gi.next()

class MyException(Exception):
    def __str__(self):
        return {}[0]

def f():
    raise MyException()
f()
class MyException(Exception):
    def __str__(self):
        return {}[0]

def f():
    yield MyException()
f()

class Base(type):
    def __setattr__(
