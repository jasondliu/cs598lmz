import socket
import struct
import sys
import time

# because i'm lazy
_s = lambda x: struct.pack('>H', x)
_u = lambda s: struct.unpack('>H', s)[0]

# all events must have a dict as docstring,
# with the keys 'event', 'data', and 'status'
# (and maybe 'kind')
# events look like this:
# d = {'event': 'event_name', 'data': 'args', 'status': 'status'}
# each key from the dict is stored in a field of the same name,
# with the exception of 'status', that is stored in a field named "status_str"
# all these fields are accessible through the __getattr__() method
# kind is not stored and is not accessible through the __getattr__() method
class Event(object):
    def __init__(self, event, data, status):
        self.event = event
        self.data = data
        self.status = status
        self.status_str = status
        self.status_code = "2.00"
