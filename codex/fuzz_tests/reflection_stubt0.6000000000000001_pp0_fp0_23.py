fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi.gi_code
fn()

# This used to crash the interpreter.  Issue #10552.
def test():
    import collections
    class A(collections.MutableMapping):
        def __init__(self):
            self.d = {}

        def __len__(self):
            return len(self.d)

        def __getitem__(self, key):
            return self.d[key]

        def __setitem__(self, key, value):
            self.d[key] = value

        def __delitem__(self, key):
            del self.d[key]

        def __iter__(self):
            return self.d.__iter__()

        def __repr__(self):
            return self.d.__repr__()

    a = A()
    a["a"] = 1
    a["b"] = 2
    a["c"] = 3
    a["d"] = 4
    print(a)

    d = {k:v for k, v in a.items()}
    print(d
