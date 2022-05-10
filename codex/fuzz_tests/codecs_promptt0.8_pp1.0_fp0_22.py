import codecs
# Test codecs.register_error() to replace unicode decode error handling

import sys
import codecs

def handler(exception):
    print 'handler:', exception

def main():
    # In real code you would use a "codec name" instead of the literal
    # encoding string 'utf-8'.
    try:
        codecs.lookup_error('test')
        print 'lookup'
    except LookupError:
        pass
    try:
        codecs.register_error('test', handler)
    except LookupError:
        pass
    try:
        codecs.lookup_error('test')
    except LookupError:
        pass
    else:
        print 'lookup passed'

    try:
        codecs.lookup_error('strict')
        print 'lookup'
    except LookupError:
        pass
    try:
        codecs.register_error('strict', handler)
    except LookupError:
        pass
    try:
        codecs.lookup_error('strict')
    except LookupError:
        pass
   
