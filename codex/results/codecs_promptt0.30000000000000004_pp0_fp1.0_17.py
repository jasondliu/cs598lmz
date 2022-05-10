import codecs
# Test codecs.register_error
#
# The codecs module is used to register the error handling
# callback for the builtin UnicodeEncodeError and
# UnicodeDecodeError exceptions.
#
# Written by Marc-Andre Lemburg (mal@lemburg.com).
#
# (c) Copyright CNRI, All Rights Reserved. NO WARRANTY.
#
# $Id: test_codecs.py,v 1.1.1.1 2006/05/30 06:01:31 hhzhou Exp $

import codecs,sys

# Error handling callback
def ignore_errors(exception):

    print '*** ignore_errors called ***'
    print 'exception:', exception
    print 'object:', exception.object
    print 'start:', exception.start
    print 'end:', exception.end
    print 'encoding:', exception.encoding
    print 'reason:', exception.reason
    print 'object[start:end]:', exception.object[exception.start:exception.end]
    print
    return (u'', exception.end)

# Register the error handler
codec
