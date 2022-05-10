import codecs
# Test codecs.register_error
from test import test_support
import StringIO, re


def encode(msg, encoding, errors='strict'):
    return msg.encode(encoding, errors)

def decode(msg, encoding, errors='strict'):
    return msg.decode(encoding, errors)

def getmessage(msg, encoding, errors='strict'):
    try:
        msg.encode(encoding, errors)
    except UnicodeEncodeError, exc:
        return exc.__class__.__name__ + ': ' + str(exc)
    else:
        raise Exception("failed to raise exception")

class dummy:
    def __init__(self, func):
        self.func = func
        self.callargs = None

    def __call__(self, *args):
        self.callargs = args
        return self.func(*args)

class StdOutCollector:
    def __init__(self):
        self.data = ''
        self.success = True

    def write(self, text):
        self.data += text


