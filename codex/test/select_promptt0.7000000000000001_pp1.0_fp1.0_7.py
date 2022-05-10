import select
# Test select.select(), reading from stdin (fd 0)
# and writing to stdout (fd 1)
# This is a no-op and should just return immediately.
# It's written like this so it doesn't need to import os
select.select([0], [1], [], 0)
# Test select.poll(), reading from stdin (fd 0)
# and writing to stdout (fd 1)
# This is a no-op and should just return immediately.
# It's written like this so it doesn't need to import os
try:
    p = select.poll()
    p.register(0, select.POLLIN)
    p.poll(0)
except AttributeError:
    # No select.poll()
    pass
# Test select.epoll(), reading from stdin (fd 0)
# and writing to stdout (fd 1)
# This is a no-op and should just return immediately.
# It's written like this so it doesn't need to import os
