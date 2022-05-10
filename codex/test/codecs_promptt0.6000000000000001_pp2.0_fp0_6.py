import codecs
# Test codecs.register_error
# Test codecs.lookup_error

# Test the error handler registry

# Test error handler lookup by name

# Test error handler lookup by function

# Test error handler lookup by class

class my_ignore_error(object):

    def __init__(self, errors='ignore'):
        self.errors = errors

    def __call__(self, exception):
        return (u'', exception.end)

class my_replace_error(object):

    def __init__(self, errors='replace'):
        self.errors = errors

    def __call__(self, exception):
        return (u'a', exception.end)

class my_xmlcharrefreplace_error(object):

    def __init__(self, errors='xmlcharrefreplace'):
        self.errors = errors

    def __call__(self, exception):
        return (u'', exception.end)

class my_backslashreplace_error(object):

    def __init__(self, errors='backslashreplace'):
        self.errors = errors

