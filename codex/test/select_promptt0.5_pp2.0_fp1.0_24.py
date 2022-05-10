import select
# Test select.select() with a selectable that doesn't have fileno()

class Foo(object):
    def __init__(self):
        self.readfds = []
        self.writefds = []
        self.exceptfds = []

    def register(self, fd, eventmask):
        if eventmask & select.POLLIN:
            self.readfds.append(fd)
        if eventmask & select.POLLOUT:
            self.writefds.append(fd)
        if eventmask & select.POLLERR:
            self.exceptfds.append(fd)

    def unregister(self, fd):
        self.readfds.remove(fd)
        self.writefds.remove(fd)
        self.exceptfds.remove(fd)

    def poll(self, timeout):
        if timeout is not None:
            raise RuntimeError("timeout argument not supported")
        return self.readfds, self.writefds, self.exceptfds


foo = Foo()
