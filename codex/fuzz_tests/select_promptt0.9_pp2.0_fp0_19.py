import select
# Test select.select without arguments.
# This should fail with a TypeError.
has_raised = False
try:
    select.select()
except TypeError:
    has_raised = True
except:
    pass

if not has_raised:
    raise RuntimeError

# We should now be able to create a socket object.
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
err = s.getsockopt(socket.SOL_SOCKET, socket.SO_ERROR)
if err != 0:
    raise RuntimeError

# Sanity check - s.getpeername() should raise an exception
# since we didn't actually connect the socket to anyone.
try:
    s.getpeername()
except socket.error, e:
    err = e.args[0]
else:
    raise RuntimeError

# Try connects - there should be no-one listening.
(r_fd, w_fd, x_fd) = select.select([ s ], [ s ], [])
if (r_fd, w_fd, x_fd) != ([ s
