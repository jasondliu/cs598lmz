import codecs
# Test codecs.register_error

def lookup(name):
    if name == "test":
        return lambda x: u"\u1234"

codecs.register_error("test", lookup)

try:
    u"\udc80".encode("utf-8", "test")
except UnicodeEncodeError, e:
    print e

try:
    u"\udc80".encode("ascii", "test")
except UnicodeEncodeError, e:
    print e

try:
    u"\udc80".encode("latin1", "test")
except UnicodeEncodeError, e:
    print e

try:
    u"\udc80".encode("utf-16", "test")
except UnicodeEncodeError, e:
    print e

try:
    u"\udc80".encode("utf-16-be", "test")
except UnicodeEncodeError, e:
    print e

try:
    u"\udc80".encode("utf-16-le", "test")
except UnicodeEncodeError
