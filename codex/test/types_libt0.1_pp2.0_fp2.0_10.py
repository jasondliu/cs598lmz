import types
types.MethodType(lambda self: None, None, Dummy)

# Test for SF bug #1465388
class C:
    def __init__(self, x=[]):
        self.x = x
    def __getitem__(self, i):
        return self.x[i]
    def __setitem__(self, i, y):
        self.x[i] = y
    def __len__(self):
        return len(self.x)

c = C()
c[:] = [1,2,3]
c[:] = [4,5,6]

# Test for SF bug #1498429
class C:
    def __init__(self, x=None):
        self.x = x
    def __getitem__(self, i):
        return self.x[i]
    def __setitem__(self, i, y):
        self.x[i] = y
    def __len__(self):
        return len(self.x)

