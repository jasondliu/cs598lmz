import codecs
# Test codecs.register_error for issue4237

import re

class MosaicSteveError(Exception):
    def __init__(self, obj):
        self.obj = obj
    def __str__(self):
        return repr(self.obj)

def handler(ex):
    return ('', ex.start + 1)

def es_se_si(exc):
    if isinstance(exc, (UnicodeDecodeError, UnicodeEncodeError)):
        newobj = MosaicSteveError(exc)
        return newobj
    else:
        raise NotImplementedError(exc)


def test_main():

    fmt = "a string %r"
    parser = re.compile(r"(?P<value>.*)")

    # Encoding
    try:
        codecs.register_error(handler, 'mosaicsteveerror')
        f = codecs.lookup_error('mosaicsteveerror')
        res = f('\xc3\xa4', 0)
        assert res == (u"\ufffd", 0), repr(res)
   
