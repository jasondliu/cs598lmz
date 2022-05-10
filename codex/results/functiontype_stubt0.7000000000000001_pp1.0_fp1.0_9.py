from types import FunctionType
a = (x for x in [1])
def f():
    """ test """
    return 1

class C:
    def __init__(self, *args):
        self.args = args
    def __str__(self):
        return "<C %s>" % str(self.args)
    def __repr__(self):
        return "C%s" % repr(self.args)
    def __getitem__(self, index):
        return C(*self.args[index])
    def __getslice__(self, i, j):
        return C(*self.args[i:j])
    def __add__(self, other):
        return C(*(self.args + other.args))
    def __radd__(self, other):
        return C(*(other.args + self.args))
    def __call__(self):
        return len(self.args)
    def __len__(self):
        return len(self.args)
    def __getattr__(self, name):
        return C(name)
    def __setattr__(self, name,
