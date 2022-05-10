import select
# Test select.select

_EPOLLIN = 0x001
_EPOLLOUT = 0x004
_EPOLLERR = 0x008 | 0x010
_EPOLLHUP = 0x010
_EPOLLET = 0x80000000
_EPOLLONESHOT = 0x40000000


class Epoll(object):

    def __init__(self):
        self.poller = select.epoll()
        self.fd_map = {}

    def register(self, fd, events):
        self.poller.register(fd, events | _EPOLLET)
        self.fd_map[fd] = fd

    def unregister(self, fd):
        del self.fd_map[fd]
        self.poller.unregister(fd)

    def modify(self, fd, events):
        self.poller.modify(fd, events | _EPOLLET)

    def poll(self, timeout):
        fd_events = self.poller.poll(timeout, 8)  # 8 means return 8 events at one time
       
