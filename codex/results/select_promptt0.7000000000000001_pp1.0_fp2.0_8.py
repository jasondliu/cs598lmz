import select
# Test select.select and select.epoll with a file descriptor
# of -1.

# select.select() and select.poll() should raise ValueError
# select.epoll() should return an epoll object

import support

import select

try:
    select.select([-1], [], [])
    raise support.TestError('select.select([-1], [], []) '
                            'should raise ValueError')
except ValueError:
    pass

try:
    select.poll().register(-1, 0)
    raise support.TestError('select.poll().register(-1, 0) '
                            'should raise ValueError')
except ValueError:
    pass

# EPOLLIN and EPOLLOUT are the only two event types supported by epoll
# (Linux 2.6.9)
e = select.epoll()
e.register(-1, select.EPOLLIN | select.EPOLLOUT)
support.compare(e.poll(), [])
e.close()
