import codecs
# Test codecs.register_error(name, error_handler)

import random

def handler(exception):
    return (u'%s' % exception.object[exception.start:exception.end],
            exception.end)

codecs.register_error('test.replace_with_name', handler)

test_cases = [
    (b'abc', 'strict'),
    (b'abc', 'test.replace_with_name'),
    ]

def print_test_case(test_case):
    bytes, error_handler = test_case
    try:
        print(bytes.decode('ignore', errors=error_handler))
    except Exception as e:
        print(e)
    try:
        print(bytes.decode('replace', errors=error_handler))
    except Exception as e:
        print(e)
    try:
        print(bytes.decode('surrogateescape', errors=error_handler))
    except Exception as e:
        print(e)

def fuzz(max_bytes=8000):
    b = bytes(random.rand
