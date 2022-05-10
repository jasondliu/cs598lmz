import types
types.MethodType(lambda self: None, None, Dummy)

# Test for SF bug #1424246
class Dummy:
    pass

class Dummy2:
    def __init__(self):
        self.__dict__ = Dummy()

# Test for SF bug #1424247
class Dummy:
    def __getattr__(self, attr):
        if attr == 'a':
            raise AttributeError
        else:
            return 1

d = Dummy()
d.a

# Test for SF bug #1424586
class Dummy:
    def __getattr__(self, attr):
        if attr == 'a':
            raise AttributeError
        else:
            return 1

d = Dummy()
d.a

# Test for SF bug #1424792
class Dummy:
    def __getattr__(self, attr):
        if attr == 'a':
            raise AttributeError
        else:
            return 1

d = Dummy()
d.a

# Test for SF bug
