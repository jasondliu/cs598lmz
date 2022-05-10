import select
# Test select.select
output = []
input = range(5)
select.select(input, output, input)
# Test select.poll
p = select.poll()
p.register(0)
p.register(sys.stdin)
p.register(sys.__stdout__)
p.unregister(1)

# Test select.poll.poll
p.poll(0)


# Test select.poll.register
p.register(sys.stdout)
p.register(sys.__stdin__)
p.register(sys.__stderr__)
# Test select.epoll
e = select.epoll()
# Test select.epoll.register
e.register(0, select.POLLIN)
# Test select.epoll.poll
e.poll(-1)
e.poll(-1, 1.0)
e.poll(-1, 1.0)
import time
time.sleep(2)

# Test select.epoll.unregister
e.unregister(0)

# Test select.kqueue
k = select.kqueue()
# Test
