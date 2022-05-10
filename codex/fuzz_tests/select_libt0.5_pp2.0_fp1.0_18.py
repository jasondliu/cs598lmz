import select
import sys
import time
import traceback

from . import util

class Poller(object):
    def __init__(self, timeout=None):
        self.timeout = timeout
        self.poller = select.poll()
        self.handlers = {}
        self.handlers_by_fd = {}
        self.handlers_by_obj = {}

    def add(self, handler, events):
        fd = handler.fileno()

        if fd in self.handlers:
            raise RuntimeError('fd %d already added' % fd)

        self.handlers[fd] = handler
        self.handlers_by_fd[fd] = handler
        self.handlers_by_obj[handler] = handler

        self.poller.register(fd, events)

    def remove(self, handler):
        fd = handler.fileno()

        if fd not in self.handlers:
            raise RuntimeError('fd %d not added' % fd)

        del self.handlers[fd]
        del self.handlers_by
