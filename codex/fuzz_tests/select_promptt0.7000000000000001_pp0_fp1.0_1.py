import select
# Test select.select
print(select.select([], [], [], 5))
print(select.select([], [], [], 0))
print(select.select([], [], [], -5))
print(select.select([], [], [], None))
print(select.select([], [], [], None))
try:
    select.select([], [], [], 'foo')
except TypeError as e:
    print(repr(e))
print(select.select([], [], [], 'foo', 'bar'))
try:
    select.select([], [], [], 1, [])
except TypeError as e:
    print(repr(e))

# Test select.poll
poll = select.poll()
print(poll.poll(-1))
print(poll.poll(0))
print(poll.poll(1))
try:
    poll.poll(None)
except TypeError as e:
    print(repr(e))
print(poll.poll(None))
try:
    poll.poll('foo')
except TypeError as e:
    print
