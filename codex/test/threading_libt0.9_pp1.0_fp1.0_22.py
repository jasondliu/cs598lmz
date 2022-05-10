import threading
threading._DummyThread._Thread__stop = lambda x: 42

from ua_parser.user_agent_parser import ParseUserAgent
from copy import copy
import struct

class Event(object):
    def __init__(self, source, name, data):
        self.source = source
        self.name = name
        self.data = data
    def __eq__(self, other):
        return (
          self.source == other.source and
          self.name == other.name and
          self.data == other.data
        )

