import codecs
# Test codecs.register_error

def handler(exception):
    return (u'', exception.end)

codecs.register_error('test.ignore', handler)

# Test that the codecs module is set up correctly

import encodings

def test(name):
    if name not in encodings.aliases.aliases:
        print "Error:", name, "not in aliases"
    if name not in encodings.aliases.aliases:
        print "Error:", name, "not in aliases"
    if name not in encodings.aliases.aliases:
        print "Error:", name, "not in aliases"

test('utf-8')
test('utf-16')
test('utf-16-le')
test('utf-16-be')
test('utf-32')
test('utf-32-le')
test('utf-32-be')
test('unicode-internal')
test('latin-1')
test('ascii')
test('charmap')
test('mbcs')
test('iso2022_jp')

