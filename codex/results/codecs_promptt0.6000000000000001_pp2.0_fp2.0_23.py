import codecs
# Test codecs.register_error
import codecs

def handler(exception):
    print('Exception:', exception)
    return ('\ufffd', 1)

codecs.register_error('test.lookup', handler)

for encoding in ['ascii', 'latin-1', 'utf-8']:
    print(encoding, ':')
    text = 'pi: \u03c0'
    try:
        print(text.encode(encoding, 'test.lookup'))
    except UnicodeEncodeError as err:
        print('ERROR:', err)
    print()

# Test codecs.encode()
print('\nTest codecs.encode()\n')

for encoding in ['ascii', 'latin-1', 'utf-8']:
    print(encoding, ':')
    text = 'pi: \u03c0'
    try:
        print(codecs.encode(text, encoding, 'test.lookup'))
    except UnicodeEncodeError as err:
        print('ERROR:', err)

