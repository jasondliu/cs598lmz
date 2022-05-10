import codecs
# Test codecs.register_error()

import codecs

def search_function(encoding):
    if encoding == 'test.searchfunction':
        return codecs.lookup('utf-8')
    return None

codecs.register(search_function)

print(codecs.encode('abc', 'test.searchfunction'))

print(codecs.encode('abc', 'test.searchfunction', 'xmlcharrefreplace'))

print(codecs.encode('abc', 'test.searchfunction', 'xmlcharrefreplace', 'ignore'))

print(codecs.encode('abc', 'test.searchfunction', 'xmlcharrefreplace', 'ignore', True))

print(codecs.encode('abc', 'test.searchfunction', 'xmlcharrefreplace', 'ignore', True, True))

print(codecs.encode('abc', 'test.searchfunction', 'xmlcharrefreplace', 'ignore', True, True, True))

print(codecs.encode('abc', 'test.searchfunction', 'xmlcharrefreplace', 'ignore',
