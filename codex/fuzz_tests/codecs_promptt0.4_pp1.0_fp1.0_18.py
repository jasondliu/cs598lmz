import codecs
# Test codecs.register_error()

import codecs

def look_for_codec(encoding):
    try:
        codec = codecs.lookup(encoding)
    except LookupError:
        print "Unknown encoding:", encoding
    else:
        print "Codec for %s is %s" % (encoding, codec.name)

look_for_codec("ascii")
look_for_codec("bogus")

def search_function(encoding):
    if encoding == "bogus":
        return codecs.lookup("ascii")
    return None

codecs.register(search_function)

look_for_codec("bogus")

# $ python codecs_register_error.py
#
# Codec for ascii is ascii
# Unknown encoding: bogus
# Codec for bogus is ascii

# The codecs module provides a number of functions and classes to help
# with encoding and decoding data to and from Python unicode strings.
#
# The codecs module also defines a set of base classes which define the
