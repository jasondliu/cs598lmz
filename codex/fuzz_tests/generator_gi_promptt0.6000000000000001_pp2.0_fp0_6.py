gi = (i for i in ())
# Test gi.gi_code.co_flags
print(gi.gi_code.co_flags)

"""
It is possible to create generators that are not iterators.
For example, the following generator is not an iterator:
"""
def gen_gen():
    yield 1
    return

gg = gen_gen()
print(gg)
# print(next(gg))
"""
It is also possible to create iterators that are not generators.
For example, the following iterator is not a generator:
"""

# class GenIter:
#     def __iter__(self):
#         return self
#     def __next__(self):
#         return 0
#
# gi = GenIter()
# print(next(gi))

# The following generator is an iterator, but not an iterable:

def gen():
    yield 1

g = gen()
# print(next(g))

"""
It is possible to create iterables that are not generators.
For example, the following iterable is not a generator:
"""

# class GenIter:
#     def __iter__(self):
#
