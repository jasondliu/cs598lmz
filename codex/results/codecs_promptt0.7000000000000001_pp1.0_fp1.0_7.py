import codecs
# Test codecs.register_error()

import codecs

def R(errors, unicode, reason):
    # return replacement character
    return u"", 0

def E(errors, unicode, reason):
    # raise an exception
    raise UnicodeDecodeError(errors, unicode, 0, 1, reason)

def I(errors, unicode, reason):
    # ignore the character
    return u"", 0

def X(errors, unicode, reason):
    # return the character unchanged
    return unicode, 1

def T(errors, unicode, reason):
    # replace with a string
    return u"test", 4

def U(errors, unicode, reason):
    # replace with a Unicode character
    return u"\u1234", 1

def C(errors, unicode, reason):
    # replace with a Unicode character
    return u"\u1234", 1

# Test 'strict'
print "strict"
for f in (R, E, I, X):
    codecs.register_error("strict", f)
    try:
       
