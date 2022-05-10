import codecs
# Test codecs.register_error

import codecs

def bad_decode(input, errors='strict'):
    return (u'', len(input))

def bad_encode(input, errors='strict'):
    return (u'', len(input))

codecs.register_error('test.notanencoding', bad_decode)
codecs.register_error('test.notanencoding', bad_encode)

# Test that the codecs module can be imported
import codecs

# Test that the encodings package can be imported
import encodings

# Test that the encodings package has at least one encoding
assert len(encodings.aliases.aliases) > 0

# Test that the encodings package has at least one codec search function
assert len(encodings.codecs.__all__) > 0

# Test that the encodings package has at least one normalizer
assert len(encodings.normalize.__all__) > 0

# Test that the encodings package has at least one incrementaldecoder
assert
