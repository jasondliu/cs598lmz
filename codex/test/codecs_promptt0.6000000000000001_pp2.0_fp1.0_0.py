import codecs
# Test codecs.register_error
class my_error(Exception):
    pass
def my_error_handler(exception):
    return (u"", exception.end)
codecs.register_error("my_error", my_error_handler)
def my_decode(input, errors='strict'):
    raise my_error
codecs.register(my_decode)
# 1st test: error handler given as name
