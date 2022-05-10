from types import FunctionType
list(FunctionType(1, 2, 3, 4, 5, 6, 7, 8, 9, 10))

# Test __reversed__.
class C(object):
    def __reversed__(self):
        return [4, 3, 2, 1]

list(reversed(C()))

# Test __contains__.
class D(object):
    def __contains__(self, x):
        return x in [1, 2, 3, 4, 5]

1 in D()

# Test __getitem__.
class E(object):
    def __getitem__(self, x):
        return x * x

list(E()[3:9:2])

# Test __getitem__ with slice object.
class F(object):
    def __getitem__(self, x):
        return x.start + x.stop

list(F()[slice(1, 2)])

# Test __getitem__ with negative indices.
class G(object):
    def __getitem__(self, x):
        return x


