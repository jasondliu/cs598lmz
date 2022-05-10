gi = (i for i in ())
# Test gi.gi_code (C->c,i)
print(isinstance(gi.gi_code, types.CodeType))

# Iterator is not hashable.
try:
    {}[gi] = 0
except TypeError:
    pass
else:
    print('TypeError not raised')
# Iterator is not hashable.
try:
    set([gi])
except TypeError:
    pass
else:
    print('TypeError not raised')

# Test an iterator with a __length_hint__ method.
class LengthHintIter:
    def __iter__(self):
        return self

    def __next__(self):
        return 42

    def __length_hint__(self):
        return 100

lh = LengthHintIter()
print(len(lh), lh.__length_hint__())

# Test an iterator with a __reduce__ method.
class ReduceIter:
    def __init__(self, x):
        self.x = x

    def __reduce__(self):
        return self.__class__, (self.
