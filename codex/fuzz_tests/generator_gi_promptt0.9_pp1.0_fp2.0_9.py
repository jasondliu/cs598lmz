gi = (i for i in ())
# Test gi.gi_code.co_flags & CO_ITERABLE_COROUTINE (1 << 26):
assert gi.gi_code.co_flags & 67108864


def close_self(gen):
    gen.close()


# Check that generator-iterator can be closed.
gi = (i for i in ())
close_self(gi)
try:
    next(gi)
except StopIteration:
    pass
else:
    assert False, "gi object is not closed"


# Test iterator protocol
class seq:
    def __init__(self, seqn):
        self.seqn = seqn

    def __iter__(self):
        return self

    def __next__(self):
        self.seqn -= 1
        if self.seqn < 0:
            raise StopIteration
        else:
            return self.seqn


for i in seq(10):
    pass

try:
    for i in seq(10):
        if i % 5 == 0:
            break
except StopIteration:
    pass
else:
    assert False, "
