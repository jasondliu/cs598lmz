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

def test_useragent_parser_with_known_networks():
    tests = [
        'Mozilla/5.0 (Linux; U; Android 4.1.1; en-us; [network] Build/JRO03C) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30',
        'Mozilla/5.0 (Linux; Android 4.0.4; Galaxy Nexus Build/IMM76B) AppleWebKit/535.19 (KHTML
