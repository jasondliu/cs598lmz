import select
# Test select.select()
# select.select([], [], [])

# Test select.poll()
# poll = select.poll()
# poll.register(1, select.POLLIN)
# poll.poll()

# Test select.epoll()
# epoll = select.epoll()
# epoll.register(1, select.EPOLLIN)
# epoll.poll()

# Test select.kqueue()
# kqueue = select.kqueue()
# kqueue.control([select.kevent(1, select.KQ_FILTER_READ, select.KQ_EV_ADD)], 0)
# kqueue.control([], 1)

# Test select.devpoll()
# devpoll = select.devpoll()
# devpoll.register(1, select.POLLIN)
# devpoll.poll()


# Test socket
import socket
# Test socket.socket()
# socket.socket()

# Test socket.socketpair()
# socket.socketpair()

# Test socket.fromfd()
# socket.fromfd(1, socket.AF_
