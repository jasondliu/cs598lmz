import codecs
# Test codecs.register_error
import _codecs
import encodings

def test_main():
    # Test codecs.register_error
    #
    # First, we test the default error handlers
    #
    # Strict
    for encoding in ('ascii', 'latin-1', 'utf-8'):
        assert codecs.lookup_error('strict') == codecs.lookup_error(encoding)
    #
    # Ignore
    assert codecs.lookup_error('ignore') == codecs.lookup_error('ascii')
    #
    # Replace
    assert codecs.lookup_error('replace') == codecs.lookup_error('ascii')
    #
    # XMLcharrefreplace
    assert codecs.lookup_error('xmlcharrefreplace') == codecs.lookup_error('ascii')
    #
    # Backslashreplace
    assert codecs.lookup_error('backslashreplace') == codecs.lookup_error('ascii')
    #
    # Now, we register a new error
