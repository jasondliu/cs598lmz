import codecs
# Test codecs.register_error

def handle_bad_bytes(exception):
    print('Got exception:', exception)
    print('  object =', exception.object)
    print('  start =', exception.start)
    print('  end =', exception.end)
    print('  reason =', exception.reason)
    print('  encoding =', exception.encoding)
    print('  startswith(object, "\\x00") =', repr(exception.object.startswith('\x00')))
    return ('', exception.end)

codecs.register_error('test.handler', handle_bad_bytes)
print('codecs.strict_errors =', codecs.strict_errors)
codecs.strict_errors = 'test.handler'
print('codecs.strict_errors =', codecs.strict_errors)

print('\nTest 1')
