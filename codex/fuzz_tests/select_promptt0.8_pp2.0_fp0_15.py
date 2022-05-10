import select
# Test select.select with invalid types
try:
    select.select(1, 2, 3, 4, 5)
except TypeError:
    pass
else:
    raise Exception, "select.select accepted invalid types"
# Test poll.poll with invalid types
try:
    select.poll().poll(1)
except TypeError:
    pass
else:
    raise Exception, "poll.poll accepted invalid types"

# Test select.select for various timeouts
for timeout in [0.0, 0.1, 1.0, -1.0]:
    (i, o, e) = select.select([], [], [], timeout)
    assert not i and not o and not e, "%s: %s %s %s" % (timeout, i, o, e)

# Test select.poll object
p = select.poll()
#
# Test poll.poll() with a timeout
assert p.poll(1000) == [], "poll.poll() should return empty list"
# Test poll with no fds registered
assert p.poll(1) == [], "poll.poll() should return empty list
