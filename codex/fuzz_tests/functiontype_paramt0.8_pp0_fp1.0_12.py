from types import FunctionType
list(FunctionType(-1, -1, 0, '', (), (), (), ''))
###############################################################################
# Test that TypeErrors raised in the iterator are caught, and the iterator is
# closed.
def count(n):
    try:
        for i in range(n):
            yield i
    finally:
        print('done')

it = count(2)
next(it)
try:
    list(it)
except TypeError:
    print('TypeError')
###############################################################################
# Test that StopIteration raised in the iterator are caught, and the iterator is
# closed.
def count(n):
    try:
        for i in range(n):
            yield i
    finally:
        print('done')

it = count(2)
next(it)
next(it)
list(it)
