import codecs
# Test codecs.register_error()

import codecs

def my_errorhandler(exception):
    print('my_errorhandler:', exception)
    return ('', exception.end)

codecs.register_error('test.myerror', my_errorhandler)

text = 'pi: \u03c0'
print(text.encode('ascii', 'test.myerror'))

# Test codecs.lookup()

import codecs

def my_search_function(encoding):
    if encoding == 'test.myencoding':
        return codecs.lookup('utf-8')
    return None

codecs.register(my_search_function)

print(codecs.encode('abc', 'test.myencoding'))

# Test codecs.encode()

import codecs

print(codecs.encode('abc', 'rot-13'))

# Test codecs.decode()

import codecs

