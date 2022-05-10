import select
# Test select.select to see if network is active
# See:  http://docs.python.org/2/library/select.html

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('localhost', 9999))
s.listen(1)

# Polling with select
# poll() returns a list of (fileobj, event) tuples
# Events can be either POLLIN, POLLOUT, or POLLERR
# Use bitwise OR to specify multiple events
# Example:  events = select.POLLIN | select.POLLOUT
# If timeout is negative, wait indefinitely
# If timeout is zero, do not block, return immediately
# wait between 0 and timeout seconds and return
# POLLIN is triggered when there is data to be read
# POLLOUT is triggered when a socket is ready for sending
# POLLERR is triggered when an error occurs

# Create a poll object
p = select.poll()
# Register the poll for input events
p.register(s, select.POLLIN)
# Poll the socket for events
