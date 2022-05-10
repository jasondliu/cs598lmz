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
