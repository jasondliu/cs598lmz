import codecs
# Test codecs.register_error()
import codecs

def search_function(encoding):
    if encoding == "test.errorhandler":
        return codecs.getencoder("ascii")
codecs.register(search_function)

def test(encoding):
    print("Registering error handler for", repr(encoding))
    codecs.register_error("test.errorhandler", codecs.ignore_errors)
    try:
        s = "abc\u1234"
        print("Before .encode():", repr(s), type(s))
        b = s.encode(encoding)
        print("After .encode():", repr(b), type(b))
        print("Decoding:", repr(b.decode(encoding)))
    except Exception as err:
        print("Error:", err)
    finally:
        codecs.lookup_error("test.errorhandler")
        codecs.register_error("test.errorhandler", None)
        print()

print("Testing search_function():")
