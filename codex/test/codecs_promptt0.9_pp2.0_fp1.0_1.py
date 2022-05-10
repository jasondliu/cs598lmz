import codecs
# Test codecs.register_error()

#
# Coders
#
def test_register_error():
    # Issue #15729: Test codecs.register_error, use names which don't mask
    # existing exceptions, add two for this test (and delete them later):
    # (Inserting at type position 1 comes naturally from test_exceptions.py)
    REGISTERED_EXCEPTIONS_NAMES = [
        ('test.test_codecs.test_register_error.testExceptionOne', None),
        ('test.test_codecs.test_register_error.testExceptionTwo', None)]

    codecs.register_error('test', lambda current, end:
        (REGISTERED_EXCEPTIONS[0](), current + 1))
    f = codecs.getencoder('test')
