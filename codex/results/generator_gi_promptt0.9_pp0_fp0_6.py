gi = (i for i in ())
# Test gi.gi_code


class G:
    "Test generator iterator getitem"
    def __init__(self, seqn):
        self.seqn = seqn
        self.count = 0
    def __iter__(self):
        return self
    def __next__(self):
        r = self.count
        self.count += 1
        if self.count > self.seqn: raise StopIteration
        return r

for i in range(10):
    assert list(G(i)) == list(range(i))

# Test mapping iterator

g = iter(tuple(map(int,"12345")))
assert hasattr(g, '__next__')
assert hasattr(g, '__length_hint__')
l1 = []
l2 = []
try:
    for i in range(1000):
        l1.append(next(g))
    for i in range(1000):
        l2.append(g.__next__())
    try:
        next(g)
    except StopIteration:
        pass
except RuntimeError:
   
