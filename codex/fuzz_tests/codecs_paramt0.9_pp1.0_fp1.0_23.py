import codecs
codecs.register_error('strict', codecs.ignore_errors)

#class Strict(codecs.StreamReader):
#    def decode(self, input, errors='strict'):
#        return codecs.strict_decode(input, self.stream, errors)
#
#def search_function(encoding):
#    if encoding == 'strict':
#        return codecs_open, codecs.StreamReader, codecs.StreamWriter
#
#codecs.register(search_function)

# register "strict" codec (similar to "replace")
# but that doesn't silently ignore errors
#
import codecs
codecs.register_error('strict', codecs.replace_errors)

def check_strict(func):

    def new_func(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except (UnicodeDecodeError, NameError, TypeError):
            print("Something went wrong with:", func)

    return new_func


def ensure_type(thing_to_check, types):

