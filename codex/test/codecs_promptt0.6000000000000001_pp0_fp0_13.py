import codecs
# Test codecs.register_error('test', test_error)
def test_error(exc):
    print(exc)
    return (u'\ufffd', exc.start + 1)
codecs.register_error('test', test_error)

s = u'\u00a0'
