import codecs
# Test codecs.register_error without defaulting to 'strict'

errors = []
def error1(exc):
    errors.append(exc)
    return '', exc.start + 1

codecs.register_error('test.error1', error1)

