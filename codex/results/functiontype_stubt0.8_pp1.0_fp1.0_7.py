from types import FunctionType
a = (x for x in [1])
b = (x for x in [2])
type(a), type(b), type(b) is type(a), type(b) is FunctionType

a.gi_frame, b.gi_frame, a.gi_frame is b.gi_frame, type(a.gi_frame) is type(b.gi_frame)

a = (x for x in [1,2,3])
a.gi_frame.f_lasti

# Test unpack_iterable (shouldn't crash)
list(zip([1,2,3], 'abc'))
tuple(zip([1,2,3], 'abc'))

# Test return value of zip()
zip()
zip([1,2,3])
zip([1,2,3], 'abc')
list(zip([1,2,3], 'abc'))

# Test when PyIter_Check fails, but PySequence_Check succeeds
import collections
zip(collections.deque('abc'), [1,2,3])
list(zip(collections.deque('abc'), [1,
