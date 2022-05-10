fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi.__code__
fn()

class C:
    def __len__(self): return 5

class D(list):
    pass

for i in range(5):
    assert len(C()) == 5
    assert len(D()) == 0
    assert len(D([1])) == 1

class C:
    def __len__(self):
        return 0

class D(C):
    def __len__(self):
        return 1

c = C()
assert len(c) == 0
assert len(D()) == 1

class R:
    def __getitem__(self, key):
        return key * 2

for i in range(5):
    assert R()[4] == 8

c = 0

class A:
    def __iter__(self):
        global c
        c += 1
        yield 5
        c += 1
        yield 6
        c += 1

it = iter(A())
for i in range(3):
    assert next(it) == 5
    assert c == 1
   
