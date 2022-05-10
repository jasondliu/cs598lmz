import codecs
# Test codecs.register_error()

def handler(exception):
    print('***', exception)
    return ' '*8, exception.end

codecs.register_error('test.replace8', handler)

