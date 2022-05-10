import codecs
# Test codecs.register_error

import codecs

def bad_errorhandler(exception):
    print('bad_errorhandler called')
    return ('', exception.end)

def good_errorhandler(exception):
    print('good_errorhandler called')
    return ('', exception.end)

def bad_errorhandler_2(exception):
    print('bad_errorhandler_2 called')
    return ('', exception.end)

def good_errorhandler_2(exception):
    print('good_errorhandler_2 called')
    return ('', exception.end)

def bad_errorhandler_3(exception):
    print('bad_errorhandler_3 called')
    return ('', exception.end)

def good_errorhandler_3(exception):
    print('good_errorhandler_3 called')
    return ('', exception.end)

def bad_errorhandler_4(exception):
    print('bad_errorhandler_4 called')
    return ('', exception.end)

def good_errorhandler_4(exception):
    print('good_error
