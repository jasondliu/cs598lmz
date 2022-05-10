import codecs
# Test codecs.register_error()

class BadContent(Exception):
    pass

class Test_register_error:
    def test_incrementalencoder(self):
        my_errors = []
        def my_handler(exception):
            my_errors.append(exception)
            return ('?', exception.end)
        codecs.register_error('test.forcing_error', my_handler)
        # XXX should test the incrementalencoder/incrementaldecoder functions
        # as well.

    def test_error_handler(self):
        my_errors = []
        def my_handler(exception):
            my_errors.append(exception)
            return '?'
        codecs.register_error('test.forcing_error', my_handler)
        # XXX should test the error_handler callback function
        # as well.

    def test_bad_error_handler(self):
        def bad_handler(exception):
            raise BadContent(exception)
        def normal_handler(exception):
            return '?'
        codecs.register_error('test.badhandler_
