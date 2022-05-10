import codecs
# Test codecs.register_error

import codecs
import sys

def r_exc(exc):
    return (None, None, exc.object[exc.start:exc.end])

def r_exc2(exc):
    return (None, None, exc.object[exc.start:exc.end] + '!')

def r_exc3(exc):
    return (None, None, 'X' + exc.object[exc.start:exc.end] + 'X')

def r_exc4(exc):
    return (None, None, 'X' + exc.object[exc.start:exc.end])

def r_exc5(exc):
    return (None, None, 'X')

def r_exc6(exc):
    return (None, None, 'X' + exc.object[exc.start:exc.end] + 'X' + exc.object[exc.start:exc.end])

