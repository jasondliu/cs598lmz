import codecs
# Test codecs.register_error

import codecs

def search_function(encoding):
    if encoding == 'test.searchfunction':
        return codecs.lookup('utf-8')
    return None

codecs.register(search_function)

u = u'\u20ac'

for encoding in ['test.searchfunction', 'utf-8']:
    print encoding, u.encode(encoding)

# Test codecs.lookup

import codecs

for encoding in ['utf-8', 'iso-8859-1', 'unknown']:
    try:
        print codecs.lookup(encoding).name
    except LookupError:
        print 'unknown encoding'

# Test codecs.getencoder

import codecs

for encoding in ['utf-8', 'iso-8859-1', 'unknown']:
    try:
        print codecs.getencoder(encoding)
    except LookupError:
        print 'unknown encoding'

# Test codecs.getdecoder

import codecs

for encoding in ['utf-8
