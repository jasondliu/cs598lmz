import select
# Test select.select()

# Create two sockets
s1, s2 = socket.socketpair()

# Create a poll object
p = select.poll()

# Register the sockets with the POLLIN event
p.register(s1, select.POLLIN)
p.register(s2, select.POLLIN)

# Send some data to s1
s1.send(b"Hello from s1")

# Poll the sockets
events = p.poll(1000)
print("events:", events)

# Read the data from the sockets
