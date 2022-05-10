import codecs
# Test codecs.register_error by registering one of the built-in
# error handlers and using it.
import codecs

register, lookup = codecs.lookup_error('strict')

def strict_error(message):
    raise TypeError(message)

codecs.register_error('strict', strict_error)

for f, e in (
    ('leer', 'strict'),
    ('leer', 'ignore'),
    ('leer', 'replace'),
    ('leer', 'xmlcharrefreplace'),
    ('leer', 'backslashreplace')
):
    try:
        lookup(e).decode(f, 'strict')
    except TypeError:
        pass
    else:
        print(e)

# Test the ability to override an encoding's incrementaldecoder
class MyIncrementalDecoder(codecs.IncrementalDecoder):
    def decode(self, input, final = False):
        return input

codecs.register(lambda c: codecs.CodecInfo(
    name = 'test79',
    encode = None,
    decode
