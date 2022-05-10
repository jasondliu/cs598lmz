import codecs
# Test codecs.register_error.

import sys

def handler(ex):
    return "^" + ex.object[ex.start:ex.end] + "^", ex.end

def test():
    e = codecs.register_error("test.strict", handler)
