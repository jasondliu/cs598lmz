import select
# Test select.select()

# Register the socket to be monitored
# Monitor the socket for read and write events
# Wait for events

#
# Create the socket with socket.socket()
# Set the socket to be non-blocking with socket.setblocking()
#

#
# Build a selector object:
# sel = selectors.DefaultSelector()
#

#
# Register the socket with selector.register()
# Register an interest in reading from the socket
#

#
# When an event happens, the selector.select() call will return a list of
# (key, events) tuples. The key is a SelectorKey namedtuple that contains a
# fileobj attribute.
#

#
# Handle the event, and unregister the socket with selector.unregister()
#


#
# change the selector to polling mode
#
# sel.close()
#
# poll = select.poll()
# poll.register(sock, select.POLLIN)
#
#
# poll.poll() will return a list of (fd, event) tuples
#
# poll.unregister(
