import codecs
# Test codecs.register_error handler for surrogateescapes
# (for testing default "surrogateescape" error handler)
# by calling back into the codecs module and indirectly
# invoking its search_function.

the_error = "surrogateescape"

def search_function(encoding):
    def encode(input, errors="strict"):
        if errors != the_error:
            raise Error("bad error handler")
    return encode

codecs.register_error(the_error, search_function)

s = '\udce2'
b = codecs.encode(s, 'utf-8', the_error)
try:
    s2 = codecs.escape_decode(b)[0]
except UnicodeDecodeError as detail:
    print("Error: {0}".format(detail))
