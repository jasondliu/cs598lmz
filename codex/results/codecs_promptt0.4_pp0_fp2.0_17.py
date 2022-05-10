import codecs
# Test codecs.register_error()

import codecs

def search_function(encoding):
    if encoding == 'test.searchfunction':
        return codecs.lookup('utf-8')
    return None

codecs.register(search_function)

# This should now work
print(codecs.encode('abc', 'test.searchfunction'))

# This should raise a LookupError
print(codecs.encode('abc', 'test.searchfunction.nonexisting'))

# This should raise a LookupError
print(codecs.encode('abc', 'test.searchfunction.nonexisting', 'replace'))

# This should raise a LookupError
print(codecs.encode('abc', 'test.searchfunction.nonexisting', 'replace', True))

# This should raise a LookupError
print(codecs.encode('abc', 'test.searchfunction.nonexisting', 'replace', True, True))

# This should raise a LookupError
print(codecs.encode('abc', 'test.searchfunction.
