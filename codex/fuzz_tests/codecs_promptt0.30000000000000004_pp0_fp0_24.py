import codecs
# Test codecs.register_error()

# This test is for the case where the error handler is a callable object
# (i.e. a class instance) which is not a subclass of the Codec class.

import codecs

class MyError(Exception):
    pass

class ErrorHandler:
    def __init__(self):
        self.called = 0
    def __call__(self, *args):
        self.called += 1
        raise MyError

def test(name):
    handler = ErrorHandler()
    codecs.register_error(name, handler)
    try:
        codecs.lookup_error(name)
    except MyError:
        pass
    else:
        print("no exception raised")
    if handler.called != 1:
        print("handler not called")

for name in ('strict', 'ignore', 'replace', 'xmlcharrefreplace',
             'backslashreplace'):
    test(name)
