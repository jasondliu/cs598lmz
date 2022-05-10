import select
# Test select.select() with a large range of file descriptors.
# Does the order in which they are given change the results?
# Does the order of the result lists change?

SIZE = 60000
results = []
for i in xrange(2):
    from random import shuffle
    l = range(SIZE)
    shuffle(l)
