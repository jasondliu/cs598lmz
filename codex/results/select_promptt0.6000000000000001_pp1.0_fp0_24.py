import select
# Test select.select
sel = select.select([], [], [], 1)
print(sel)

# Test select.poll
poll = select.poll()
poll.register(sys.stdin, select.POLLIN)
print(poll.poll(1))
