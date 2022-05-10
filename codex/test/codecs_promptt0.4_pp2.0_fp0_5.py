import codecs
# Test codecs.register_error
import codecs
import encodings

def test_register_error():
    codecs.register_error('test.strict', codecs.strict_errors)
    codecs.register_error('test.ignore', codecs.ignore_errors)
    codecs.register_error('test.replace', codecs.replace_errors)
    codecs.register_error('test.xmlcharrefreplace', codecs.xmlcharrefreplace_errors)
    codecs.register_error('test.backslashreplace', codecs.backslashreplace_errors)
    #
    # First, try to register an existing error handler
    #
    try:
        codecs.register_error('test.strict', codecs.ignore_errors)
    except ValueError:
        pass
    else:
        print('expected ValueError')
    #
    # Now, try to register an error handler under an existing name
    #
    try:
        codecs.register_error('strict', codecs.ignore_errors)
    except ValueError:
        pass
