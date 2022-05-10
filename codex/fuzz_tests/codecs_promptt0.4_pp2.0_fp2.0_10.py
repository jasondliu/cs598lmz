import codecs
# Test codecs.register_error

import codecs

def bad_errorhandler(exception):
    print "bad_errorhandler:", exception
    return (u'', exception.end)

def good_errorhandler(exception):
    print "good_errorhandler:", exception
    return (u'\uFFFD', exception.end)

def bad_incrementalencoder(exception):
    print "bad_incrementalencoder:", exception
    return u'', exception.end

def bad_incrementaldecoder(exception):
    print "bad_incrementaldecoder:", exception
    return u'', exception.end

def good_incrementalencoder(exception):
    print "good_incrementalencoder:", exception
    return u'\uFFFD', exception.end

def good_incrementaldecoder(exception):
    print "good_incrementaldecoder:", exception
    return u'\uFFFD', exception.end

def bad_streamreader(stream, errors='strict'):
    print "bad_streamreader:", stream,
