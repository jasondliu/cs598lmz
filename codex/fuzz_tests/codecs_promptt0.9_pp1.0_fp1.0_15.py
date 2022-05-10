import codecs
# Test codecs.register_error and reject error handler classes

UTF8 = 'utf-8'
registered = []

# Exception raised by error handler class.
class MyUnicodeError(UnicodeError):
    def __init__(self):
        self.object = 2222

# Helper class to return Unicode objects from test
# methods in this module.
class UnicodeReturner:
    def __init__(self, unicode, start=None, end=None):
        self.unicode = unicode
        if start:
            self.start = start
        else:
            self.start = 0
        self.end = end

# Make Python and C API happy.
# (The latter doesn't like unicode error objects and encodings with
# non-ASCII characters!)
class MyUnicodeError2(UnicodeError):
    pass

class MyUnicodeError3(UnicodeError):
    pass

class MyLookupError(LookupError):
    pass

class MyLookupError2(LookupError):
    pass

class MyLookupError3(Lookup
