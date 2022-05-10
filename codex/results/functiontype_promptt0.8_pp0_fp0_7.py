import types
# Test types.FunctionType

class F(object):
    """
    Test class for function types
    """
    def __init__(self):
        "Initializes the data"
        self.data = []

    def f(self):
        "Return 42"
        return 42

    def __len__(self):
        "Returns the length of data"
        return len(self.data)

    def __getitem__(self, i):
        "Returns the i-th element"
        return self.data[i]

    def __setitem__(self, i, item):
        "Sets the i-th element"
        self.data[i] = item

    def __delitem__(self, i):
        "Removes the i-th element"
        del self.data[i]

def f():
    "Return 42"
    return 42

def test_FunctionType():
    "Test the FunctionType type"
    assert type(f) == types.FunctionType
    assert type(F.f) == types.MethodType
    assert type(F.__init__)
