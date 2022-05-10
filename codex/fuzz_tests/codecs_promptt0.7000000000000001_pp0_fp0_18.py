import codecs
# Test codecs.register_error('strict', codecs.ignore_errors)
import codecs
assert codecs.lookup_error('strict') is codecs.ignore_errors

def test_codecs_replace_errors(test_vsn):
    """
    codecs.register_error('strict', codecs.replace_errors)
    """
    import codecs
    assert codecs.lookup_error('strict') is codecs.replace_errors


def test_codecs_xmlcharrefreplace_errors(test_vsn):
    """
    codecs.register_error('strict', codecs.xmlcharrefreplace_errors)
    """
    import codecs
    assert codecs.lookup_error('strict') is codecs.xmlcharrefreplace_errors


def test_codecs_backslashreplace_errors(test_vsn):
    """
    codecs.register_error('strict', codecs.backslashreplace_errors)
    """
    import codecs
    assert codecs.lookup_error('strict') is codecs.back
