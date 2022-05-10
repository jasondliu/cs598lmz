import select
# Test select.select()
print(select.select([sys.stdin], [], [], 20))

# Test select.poll()
p = select.poll()
p.register(sys.stdin)
print(p.poll(20))

# Test select.epoll()
epoll = select.epoll()
epoll.register(sys.stdin.fileno(), select.EPOLLIN)
events = epoll.poll(1)
#epoll.unregister(sys.stdin.fileno())
#epoll.close()
print(events)
