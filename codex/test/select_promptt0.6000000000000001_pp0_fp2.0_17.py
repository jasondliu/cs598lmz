import select
# Test select.select()
fd = os.open("/etc/hosts", os.O_RDONLY)
rs, ws, xs = select.select([fd], [], [])
print("Readable:", rs)
print("Writable:", ws)
print("Exceptions:", xs)

# Test select.poll()
poll = select.poll()
poll.register(fd, select.POLLIN | select.POLLPRI)
events = poll.poll(1000)
print("Poll events:", events)

# Test select.epoll()
epoll = select.epoll()
epoll.register(fd, select.EPOLLIN | select.EPOLLPRI)
events = epoll.poll(1000)
print("EPoll events:", events)

