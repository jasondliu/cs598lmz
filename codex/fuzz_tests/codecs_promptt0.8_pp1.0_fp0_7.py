import codecs
# Test codecs.register_error without defaulting to 'strict'

errors = []
def error1(exc):
    errors.append(exc)
    return '', exc.start + 1

codecs.register_error('test.error1', error1)

with codecs.open('does_not_exist', encoding='ascii', errors='test.error1') as f:
    try:
        f.read()
    except UnicodeError as e:
        pass
with codecs.open('does_not_exist', encoding='ascii', errors='test.error1') as f:
    try:
        f.read(23)
    except UnicodeError as e:
        pass

# Issue #15479: Test codecs.register_error with surrogateescape and
# surrogatepass.
def surrogates_error(exc):
    return None, exc.start + 1

def surrogates_handler(err_):
    raise TypeError("should use 'surrogatepass' or 'surrogateescape'")

codecs.register_error('surrogates', surrogates_error)

