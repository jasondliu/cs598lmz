import _struct,posix,time,string
import EventManager,sys,ITU
import types

class POLL:
    IN=0x100
    PRI=0x200
    OUT=0x4
    ERR=0x8
    HUP=0x10
    NVAL=0x20
    def __init__(self):
        pass

POLLIN=POLL.IN
POLLOUT=POLL.OUT
POLLERR=POLL.ERR
POLLHUP=POLL.HUP
POLLNVAL=POLL.NVAL

class Poll:
    def __init__(self):
        self.fmap={}
        self.map={}
    def register(self,fd,events):
        fd=fd.fileno()
        self.map[fd]=events
        self.fmap[fd]=events
        if self.map.has_key(0):
            self.map.has_key(0).unregister(self)
    def unregister(self,fd):
        fd=fd.fileno()

