import select
# Test select.select()
inputs = [input(), input()]
readable, writable, exceptional = select.select(inputs, [], [])
print(readable)    # a list of sockets
print(writable)    # a list of sockets
print(exceptional) # a list of sockets

# Test select.poll()
inputs = [input(), input()]
p = select.poll()
for input in inputs:
    p.register(input, select.POLLIN)
events = p.poll(5)  # This will block until timeout or events occur
print(events)        # a list of (fd, event) tuples

# Test select.epoll()
e = select.epoll()
for input in inputs:
    e.register(input, select.EPOLLIN)
events = e.poll(5)  # This will block until timeout or events occur
print(events)        # a list of (fd, event) tuples

# Test select.kqueue()
k = select.kqueue()
