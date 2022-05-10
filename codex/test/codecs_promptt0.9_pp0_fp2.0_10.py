import codecs
# Test codecs.register_error:
def errFunc():
    while True:
        yield u'\u0082'
        yield '\ufffd'
