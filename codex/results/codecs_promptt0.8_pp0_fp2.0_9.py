import codecs
# Test codecs.register_error

# This test doesn't make a lot of sense unless it's run with -u
# Read the definition of codecs.register_error() and
# codecs.lookup_error() if you want to know what's going on in some
# detail.

# The test is supposed to generate lots of warnings, but no crashes.

# A simple error handler

class error_handler(object):

    def __init__(self, *args):
        pass

    def __call__(self, *args):
        return u'x'

# A handler with a 'name' attribute

class error_handler2(object):

    name = 'test_handler'

    def __init__(self, *args):
        pass

    def __call__(self, *args):
        return u'x'

# An error handler that can't be called

class error_handler3(object):
    def __init__(self, *args):
        pass

# A handler that doesn't like its arguments

class error_handler4(object):

    def __init__(self,
