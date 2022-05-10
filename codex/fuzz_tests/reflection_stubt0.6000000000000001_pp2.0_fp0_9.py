fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi
fn()

# another approach:
# https://stackoverflow.com/questions/31995726/how-can-i-call-an-empty-generator-in-python-3
class EmptyGenerator():
    def __init__(self, *args, **kwargs):
        pass

    def __next__(self):
        raise StopIteration

    def __iter__(self):
        return self

    def send(self, value):
        pass

    def throw(self, typ, val=None, tb=None):
        pass

    def close(self):
        pass

g = EmptyGenerator()
g.__next__() # will raise StopIteration

# there is also a way to use the dis module to get the bytecode
# and then execute it, but I don't know if this is a good approach
# to the problem.

# another approach
# https://stackoverflow.com/questions/42044031/how-to-execute-the-empty-generator-in-python3
# but I do not know
