import _struct
import binascii
import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), '../lib'))
import dns_utils

class DNS_Header(object):
    def __init__(self, *args, **kwargs):
        self.id = 0
        self.flags = 0
        self.questions = 0
        self.answers = 0
        self.authority = 0
        self.additional = 0
        self.payload = kwargs.get('payload', '')

    def parse(self, data):
        (self.id, self.flags, self.questions, self.answers,
            self.authority, self.additional) = _struct.unpack('>HHHHHH', data[:12])

        self.payload = data[12:]

