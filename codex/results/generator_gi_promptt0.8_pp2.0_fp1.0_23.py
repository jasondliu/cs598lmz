gi = (i for i in ())
# Test gi.gi_code.co_name

class G:
    def __init__(self):
        self.gi = (i for i in ())

g = G()
# Test g.gi.gi_code.co_name

class G:
    def __init__(self):
        self.gi = gi = (i for i in ())

# Test object.__init__

class O:
    def __init__(self):
        self.gi = gi = (i for i in ())

# Test object.__new__

class N:
    def __new__(cls, arg=1):
        self = object.__new__(cls)
        self.gi = (i for i in ())
        return self

# Test object.__getattribute__

class G:
    def __getattribute__(self, name):
        if name == "gi":
            return (i for i in ())
        return object.__getattribute__(self, name)

# Test object.__getattr__

class G:
    def __getattr__(
