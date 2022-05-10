fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi.gi_code
fn()

# issue #9
def f():
    yield 1
f().next()

# issue #10
class A:
    def __init__(self):
        self.a = 1
    def __getitem__(self, key):
        return key
A()[1]

# issue #11
class A:
    def __init__(self, a):
        self.a = a
    def __getitem__(self, key):
        return key
A(1)[1]

# issue #12
class A:
    def __init__(self, a):
        self.a = a
    def __getitem__(self, key):
        return key
A(1)[1][2]

# issue #13
class A:
    def __init__(self, a):
        self.a = a
    def __getitem__(self, key):
        return key
A(1)[1][2][3]

# issue #14
class A:
    def __init__(self, a
