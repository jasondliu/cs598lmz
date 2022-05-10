fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi
fn()

# This should fail with a TypeError
class BadCmp:
    def __eq__(self, other):
        return other

BadCmp() == BadCmp()

# This should fail with a TypeError
class BadHash:
    def __hash__(self):
        return self

hash(BadHash())

# This should fail with a TypeError
class BadIter:
    def __iter__(self):
        return self

iter(BadIter())

# This should fail with a TypeError
class BadNext:
    def __next__(self):
        return self

next(BadNext())

# This should fail with a TypeError
class BadLen:
    def __len__(self):
        return self

len(BadLen())

# This should fail with a TypeError
class BadGetItem:
    def __getitem__(self, i):
        return self

BadGetItem()[0]

# This should fail with a TypeError
class BadSetItem:
    def __setitem__(self, i
