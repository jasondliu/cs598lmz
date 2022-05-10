import codecs
# Test codecs.register_error
def handler1(exception):
    return ("BAD", exception.end)

codecs.register_error('test.name1', handler1)

# "ignore" is special
