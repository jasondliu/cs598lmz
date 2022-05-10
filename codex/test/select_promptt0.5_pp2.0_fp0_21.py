import select
# Test select.select
fd_sets = [(), (), ()]

select.select(fd_sets[0], fd_sets[1], fd_sets[2], 0.0)

# Test select.error
try:
    select.select([], [], [], 0.0)
except select.error:
    pass

# Test select.poll
poll = select.poll()
poll.poll()

# Test select.epoll
epoll = select.epoll()
epoll.poll()

# Test select.kqueue
kqueue = select.kqueue()
kqueue.control([], 0)

# Test select.kevent
kevent = select.kevent(0, 0, 0, 0)

# Test select.devpoll
devpoll = select.devpoll()
devpoll.poll()
