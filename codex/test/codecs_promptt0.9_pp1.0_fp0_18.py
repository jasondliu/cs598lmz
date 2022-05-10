import codecs
# Test codecs.register_error()
encoding = 'undecodeable_encoding'

def problem_handler(exception):
    return ('undecodeable', 0), ('', exception.end)

