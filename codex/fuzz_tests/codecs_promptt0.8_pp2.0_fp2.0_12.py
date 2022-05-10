import codecs
# Test codecs.register_error()
def generate_error(error_name):
    def error(*args):
        print("code error: ", error_name)
        raise error_name("test")
    return error
codecs.register_error("ignore", generate_error("ignore"))
codecs.register_error("replace", generate_error("replace"))
codecs.register_error("strict", generate_error("strict"))
codecs.register_error("xmlcharrefreplace", generate_error("xmlcharrefreplace"))
codecs.register_error("backslashreplace", generate_error("backslashreplace"))
codecs.register_error("surrogateescape", generate_error("surrogateescape"))
codecs.register_error("surrogatepass", generate_error("surrogatepass"))
try:
    codecs.register_error("namereplace")
except TypeError:
    print("TypeError")

# Test codecs.codec.register_error()
import types
def generate_error(error_name):
    def error(*args):
        print("code error
