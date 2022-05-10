import selectors
import socket
import types

from . import constants
from . import helpers
from . import package_objects as po
from . import parse_objects as poo

class Event(object):

    def __init__(self, sel, fd, mask):
        self.sel = sel
        self.fileobj = fd
        self.mask = mask

    def fileno(self):
        return self.fileobj.fileno()

    def __str__(self):
        res = []
        for attr in dir(selectors):
            if attr.startswith('EVENT_'):
                flag = getattr(selectors, attr)
                if self.mask & flag:
                    res.append(attr)
        return '|'.join(res)

class Server(object):

    def __init__(self, ip_address, port, task_factory, max_task=1):
        self.sel = selectors.DefaultSelector()
        self.ip_address = ip_address
        self.port = port
        self.task_f
