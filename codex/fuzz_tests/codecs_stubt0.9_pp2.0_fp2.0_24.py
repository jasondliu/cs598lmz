import codecs

def add_one_codepoint(exc):
    return ("a", exc.start)

def add_utf16_bytes(exc):
    return (b'ab', exc.start)

def add_utf32_bytes(exc):
    return (b'abcd', exc.start)

codecs.register_error("add_one_codepoint", add_one_codepoint)
codecs.register_error("add_utf16_bytes", add_utf16_bytes)
codecs.register_error("add_utf32_bytes", add_utf32_bytes)

output_stream = codecs.getwriter('utf-16')(sys.stdout.buffer)
output_stream.write(u''.encode('utf-8', 'add_utf16_bytes'))

output_stream = codecs.getwriter('utf-32')(sys.stdout.buffer)
output_stream.write(u''.encode('utf-8', 'add_utf32_bytes'))

output_stream = codecs.getwriter('latin-1')(sys.stdout.buffer)
output_stream.write(u''.encode('utf-8', 'add_one_codepoint'))

output_stream = codecs.getwriter('utf-8')(sys.stdout.buffer)
output_stream.write(u''.encode('utf-8', 'add_one_codepoint'))

output_stream = codecs.getwriter('utf-8')(sys.stdout.buffer)
output_stream.write(u''.encode('utf-8', 'strict'))
