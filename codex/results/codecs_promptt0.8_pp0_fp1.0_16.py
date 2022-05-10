import codecs
# Test codecs.register_error

import codecs

# Test a few codecs
for codec in ('iso-8859-1',
              'charmap',
              'cp037',
              'utf-8-sig',
              'utf-16',
              'utf-32'):
    try:
        with open('nothing', 'w', encoding=codec) as f:
            f.write('\xff')
    except UnicodeEncodeError:
        pass

# Test a few encodings that do not have a codec
for encoding in ('base64', 'quopri', 'uu', 'hex_codec'):
    with open('nothing', 'w', encoding=encoding) as f:
        f.write('\xff')

# An encoding with no error handler
def strict_error_func(exc):
    if isinstance(exc, UnicodeEncodeError):
        return u'', exc.end
    else:
        raise TypeError("encoding with no error handler")

codecs.register_error('strict', strict_error_func)
with open('nothing', '
