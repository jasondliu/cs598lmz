import _struct
# Test _struct.Struct()
class mystruct(object):
    def __init__(self, theformat):
        self.theformat = theformat
        self.thestruc = _struct.Struct(theformat)

    def unpack(self, thestring):
        return self.thestruc.unpack(thestring)

    def pack(self, *args):
        return self.thestruc.pack(*args)

Struct = mystruct

from socket import socket, _LOCALHOST, _LOCALHOST_V6, gethostname, \
     getaddrinfo, error, has_ipv6
from time import time

from eventloop import EventLoop, TaskletExit, QUIT, ALARM
from lib_pypy import _testcapimod
import module

from stacklessapi import coro_bind, coro_unbind

from stackless import schedule, stack_size, enable_softswitch, disabled, getruncount
from stackless import choose_runnable, schedule_remove, \
    schedule_put, run, stack_current, softswitch, runcount
