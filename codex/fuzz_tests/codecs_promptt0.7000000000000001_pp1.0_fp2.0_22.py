import codecs
# Test codecs.register_error()
def replace_error(error):
    return (u'\ufffd', error.end)
codecs.register_error('replace_error', replace_error)

import os

def test_convert_to_internal(tmpdir):
    """Test the convert_to_internal() function."""
    # test default encoding
    assert convert_to_internal('/tmp/äöü', 'utf-8') == '/tmp/äöü'
    assert convert_to_internal('/tmp/äöü', 'utf-16') == '/tmp/\x00ä\x00ö\x00ü'
    assert convert_to_internal('/tmp/äöü', 'utf-32') == '/tmp/\x00\x00\x00ä\x00\x00\x00ö\x00\x00\x00ü'
    assert convert_to_internal('/tmp/äöü', 'utf-16-le') == '/tmp/ä\x00ö\x00ü\x00'
    assert convert_to_internal('/tmp/ä
