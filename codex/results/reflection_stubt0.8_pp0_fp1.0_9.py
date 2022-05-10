fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi = (i for i in ())
gi.gi_frame.f_code = fn.__code__
gi.gi_frame.f_locals = {}

# yield from support
# See http://www.python.org/dev/peps/pep-0342/
import collections

def __next__(self):
    return self

def __iter__(self):
    return self

class __await__:
    def __init__(self, obj):
        self.obj = obj
    def __iter__(self):
        return self
    def __next__(self):
        return self.obj
    def send(self, value):
        raise StopIteration(value)
    def throw(self, type, value=None, traceback=None):
        raise StopIteration(type)
    def close(self):
        pass

class __aiter__:
    def __init__(self, obj):
        self.obj = obj
    def __await__(self):
        return self.obj.__await__()


class
